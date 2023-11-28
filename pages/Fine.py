#this is visible to student only ; it displayes if any fines were availabe. 


#allowed to be rendered only for the students. 

import streamlit as st;
from streamlit_extras.switch_page_button import switch_page
from Models import Book,Reserve,report,Fine;

#check for admin user logged 


if st.session_state["User_ID"]==None:
    #switch the page to the Login.py
    switch_page("Login");
else:
    if st.session_state["Type"]=="Student":
        #now write the logic for search 
        

        #show the information with st.warning() if u have the fine. 

        st.header("Student Fines Page")

        student_fines = Fine.fetch_student_fines(st.session_state["conn"],st.session_state["ID"]);
        # Container to organize the layout
        if len(student_fines)>0:

            # Create an empty container
            placeholder = st.empty()

            # Display fines in the main container
            with placeholder.form("Fines page"):
                if not student_fines:
                    st.info("You have no fines.")
                else:
                    total_amount=0;
                    for fine in student_fines:
                        col1,col2= st.columns(2)
                        with col1:
                            st.write(f"Fine ID: {fine[0]}")
                            st.write(f"Book Name: {fine[4]}")
                            if fine[1]==1:
                                st.write(f"Book Returned: "+" Yes");
                            else:
                                st.write(f"Book Returned: "+" No");
                        with col2:
                            st.write(f"Student Name: {fine[1]}")
                            st.write(f"Deadline: {fine[2]}")
                            st.write(f"Fine Amount: {fine[3]}")
                        st.write("-" * 50)
                        total_amount = total_amount +  int(fine[3]);
                    st.text("Total Fine amount : " + str(total_amount))
                    payment = st.form_submit_button("paynow")              
        else: 
            st.info("NO pending fines associated with your account");

    else:
        st.info(" Fines is only for students domain to check whether any fines associated with account")