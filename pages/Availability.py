# show the list of available books with their quantity in the admin profile; 
#it shows access denied.
import streamlit as st;
import pandas as pd;
from streamlit_extras.switch_page_button import switch_page
from Models import Book;
if "User_ID" in st.session_state and st.session_state["User_ID"]==None:
    #switch the page to the Login.py
    switch_page("Login");
else:
    #show in the tables; 
    if "Type" in st.session_state and st.session_state["Type"]=="Admin":
        #show the logic for the admin to eb seen; 
        #select * from books; 
        df = Book.read_books(st.session_state["cursor"]);
        #show the in a table;
        columns=("Book_id","Book Name","Book Author","Book Year","Quantity")
        data = pd.DataFrame(df, columns=("Book_id", "Book Name", "Book Author", "Book Year", "Quantity"))
        data = data.drop('Book_id', axis=1)
        st.table(data);
    else:
        st.info(" This only allowed for adminstrators display !!!");
    