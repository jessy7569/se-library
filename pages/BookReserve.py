#this is used for reservign a book from the student profile. 


import streamlit as st;
from streamlit_extras.switch_page_button import switch_page
from Models import Book,Reserve,report;

#check for admin user logged 


if st.session_state["User_ID"]==None:
    #switch the page to the Login.py
    switch_page("Login");
else:
    if st.session_state["Type"]=="Student":
        #now write the logic for search 
        st.subheader("Book Reservation Form")

        # Fetch available book names for the dropdown
        available_books = Book.fetch_available_books(st.session_state["conn"])

        # Dropdown for selecting book name
        selected_book = st.selectbox("Select Book", options=[name for name, _ in available_books])

        #write some st.markdown to display the book details using the html page;
        # Get the corresponding book ID based on the selected name
        selected_book_id = [book_id for name, book_id in available_books if name == selected_book][0]

        student_id = st.session_state["ID"];
        reservation_date = st.date_input("Reservation Date", None)
        status = st.selectbox("Reservation Status", options=["reserved", "returned"])

        #defaulting the diable to false;
        st.session_state["disabled"]=False;
        
        if (report.check_report_existence(st.session_state["conn"],st.session_state["cursor"],student_id)):
            st.warning("report exists and Book reservation is being disabled !!!");
            st.session_state["disabled"]=True;
        
        if st.button("Reserve Book",disabled=st.session_state["disabled"]):
            
            if student_id and reservation_date and status:
                try:
                    Reserve.reserve_book(st.session_state["conn"], st.session_state["cursor"], student_id, selected_book_id, status='reserved')
                    st.success("Book reserved successfully!")
                except Exception as e:
                    st.error(f"Error reserving book: {e}")
            else:
                st.warning("Please fill in all fields.")
    else:
        st.info("Only students can reserve a book");