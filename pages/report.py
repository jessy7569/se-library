#this page has only access to admin roles and not for user roles. 
import streamlit as st;
from streamlit_extras.switch_page_button import switch_page
from Models import report,Student,Fine,Book,Reserve;
if st.session_state["User_ID"]==None:
    #switch the page to the Login.py
    switch_page("Login");
else:
    if (st.session_state["Type"]=="Admin"):
        #render the elements on the Screen ;
        #to report a student from it.
        st.subheader("Enter Report Data")

        #fetch details from the student table;
        students = Student.fetch_student_names(st.session_state["conn"],st.session_state["cursor"]);
        selected_student = st.selectbox("Select Student", options=[name for name, _ in students])
        # lib_id = st.text_input("Library Admin ID", "");
        
        # Get the corresponding student ID based on the selected name
        student_id = [student_id for name, student_id in students if name == selected_student][0]

        if student_id:
                books_by_student = Book.fetch_books_by_student(st.session_state["conn"],student_id)
                # Dropdown for selecting book name
                if books_by_student:
                    selected_book = st.selectbox("Select Book", options=[name for name, _ in books_by_student])
                    selected_book_id = [book_id for name, book_id in books_by_student if name == selected_book][0]
                    book_returned = st.checkbox("Is the book returned?")
                    deadline = st.date_input("Deadline for Return", None)
                    fine_amount = st.number_input("Fine Amount", min_value=0.5,help="first 10 days each day $1 , from there every 10 days it gets doubled.")
                    report_description = st.text_area("Report Description", "")
                    report_date = st.date_input("Report Date", None)

                    lib_id = st.session_state["ID"];
                    submit = st.button("Submit");

                    if submit:
                        if student_id  and report_description and report_date:
                            try:
                                report.insert_report_data(st.session_state["conn"],st.session_state["cursor"],student_id, st.session_state["ID"], report_description, report_date)
                                #update the fine table simultanesouly 
                                Fine.insert_fine_data(st.session_state["conn"],book_returned, deadline, fine_amount, student_id,selected_book_id, lib_id)
                                #update the book reservation table with the status as returned.
                                Reserve.book_returned(st.session_state["conn"],st.session_state["cursor"],student_id,selected_book_id);
                                st.success("Report has been added on to the student")
                            except Exception as e:
                                st.error(f"Error inserting data into the database: {e}")
                        else:
                            st.warning("Please fill in all fields.")
                else:
                    st.info(" there are no books reserved with the student id ");
    else:
        st.warning("Access denied Only admins can post report on student !!!");
