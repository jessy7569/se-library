

import streamlit as st;

def create_student(con,cursor, student_id, first_name, last_name, h_no, street, city, zipcode, telephone_number, user_id):
    sql = "INSERT INTO Student (Student_ID, First_Name, Last_Name, H_No, Street, City, Zipcode, Telephone_Number, User_ID) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (student_id, first_name, last_name, h_no, street, city, zipcode, telephone_number, user_id)
    cursor.execute(sql, values)
    con.commit()
    return "Student added successfully!";

def fetch_student_names(con,cursor):
    cursor = con.cursor()
    cursor.execute("SELECT Student_ID, First_Name, Last_Name FROM Student")
    students = cursor.fetchall()
    return [(f"{student[1]} {student[2]}", student[0]) for student in students]

def fetch_student_id_from_user_id(con,user_id):
    cursor = con.cursor()
    query = "SELECT Student_ID FROM Student WHERE User_ID = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    if result:
        st.session_state["ID"]=result[0];
        return result[0]  # Return the fetched student_id
    else:
        return None 