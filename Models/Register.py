import streamlit as st;
from Models import Student,Admin;
# Register a student in the Registration table
def register_student(con,cursor, user_id, email_id, password, user_type='Student'):
    sql = "INSERT INTO Registration (User_ID, Email_id, Password, Type) VALUES (?, ?, ?, ?)"
    values = (user_id, email_id, password, user_type)
    cursor.execute(sql, values)
    con.commit()
    print("Student registered successfully!");
    return True;

# Login authentication on Registration table;
def authenticate_login(con,cursor, email_id, password):
    sql = "SELECT * FROM Registration WHERE Email_id = ? AND Password = ?"
    values = (email_id, password)
    cursor.execute(sql, values)
    user = cursor.fetchone()
    if user:
        print(user);
        st.session_state["User_ID"] = user[0];
        st.session_state["Type"]= user[3];
        print(st.session_state)
        print("Login successful!")
        if (st.session_state["Type"]=="Student"):
            Student.fetch_student_id_from_user_id(con,user[0]);
        elif (st.session_state["Type"]=="Admin"):
            Admin.fetch_admin_id_from_user_id(con,user[0]);
        return True
    else:
        print("Invalid login credentials. Please check your email and password.")
        return False


