import streamlit as st; 
from  connect_to_db import connection_parametrs;
from Models import Student,Register,Admin;
from streamlit_extras.switch_page_button import switch_page

conn,cursor = connection_parametrs.connection();

st.header("Library Management System")

#load the connection details into the st.session_state variable for future usage in other pages;
st.session_state["conn"]=conn;
st.session_state["cursor"]=cursor;
option = st.selectbox(
    '',
    ('Login', 'SignUp'));

if option=="Login":

    #render username on to the screne and password; 
    email = st.text_input("Email_id")
    password = st.text_input("Password", type="password")
    Login = st.button("Login");

    if Login:
    #store the user_id variable into this and Type associated in the table. 
    
    #logical test for logging into the application;
        if (Register.authenticate_login(conn,cursor, email, password)):
            #store the user_id into the session variable and tyep as well; 
            switch_page('Availability');
        else:
            st.error("Incorrect username or password !!!");
    
    
elif option=="SignUp":
    #create for student and admin different sign in forms;
    # reate the form for student and then for admin registration ; 
    user_id = st.text_input("User_ID");
    email = st.text_input("Email_id")
    pwd = st.text_input("Password", type="password")
    cpwd = st.text_input("Confirm Password", type="password")
    Type = st.selectbox("Role student/admin ? ",('Student','Admin') );
    if Type =="Student":
        st.markdown("Student Register Form");
        first_name = st.text_input("FirstName");
        last_name = st.text_input("LastName");   
        h_no = st.text_input("Hno");
        street = st.text_input("Street");
        city = st.text_input("City");
        zipcode = st.text_input("ZipCode");
        telephone_number = st.text_input("TelephoneNumber");

    elif Type == "Admin":
        name = st.text_input("Name");
    Reg = st.button("Register")
    if Reg:
        if Type == "Student":
            #check for firstname and lastname mandatory fields. 
            if first_name == "" or last_name =="":
                st.error(" First name and last name are required fields");
            elif pwd!=cpwd:
                st.error(" password and confirm password doesnot match !")
            else:
                #send the details to the backend to db;
                #first send some details into the student;
                res = Register.register_student(conn,cursor, user_id, email, pwd)
                # Add the student to the Student table
                stu = Student.create_student(conn,cursor, user_id, first_name, last_name, h_no, street, city, zipcode, telephone_number, user_id)
                if(res==True and stu == "Student added successfully!"):
                    st.success(" Student registred sucessfully.");
                    st.info("please use the email and password for loggind into your accoutn");

        elif Type == "Admin":
            #name is mandotory field
            if name=="":
                st.error(" please enter your name .")
            res = Admin.create_library_admin(conn,cursor,user_id, email, pwd, user_id, name);
            #insert into the databse; 
            st.success(res);
            st.info("please use the email and password for loggind into your account ");