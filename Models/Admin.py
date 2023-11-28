
import streamlit as st;

def create_library_admin(conn,cursor,user_id, email_id, password, lib_id, lib_name):
    # Insert into Registration table
    sql = "INSERT INTO Registration (User_ID, Email_id, Password, Type) VALUES (?, ?, ?, ?)"
    values = (user_id, email_id, password, "Admin");
    cursor.execute(sql, values)
    conn.commit()
    

    # Insert into LibraryAdmin table
    sql_library_admin = "INSERT INTO LibraryAdmin (Lib_id, Lib_Name, User_ID) VALUES (?, ?, ?)"
    values_library_admin = (lib_id, lib_name, user_id)
    cursor.execute(sql_library_admin, values_library_admin)

    conn.commit()
    return "Library admin created successfully!";


def fetch_admin_id_from_user_id(con,user_id):
    cursor = con.cursor()
    query = "SELECT Lib_id FROM LibraryAdmin WHERE User_ID = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    if result:
        st.session_state["ID"]=result[0];
        return result[0]  # Return the fetched student_id
    else:
        return None 