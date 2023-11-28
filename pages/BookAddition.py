#book addition is possible only to the admin user;
import streamlit as st;
from streamlit_extras.switch_page_button import switch_page
from Models import Book;

#check for admin user logged 

import streamlit as st;
from streamlit_extras.switch_page_button import switch_page

if st.session_state["User_ID"]==None:
    #switch the page to the Login.py
    switch_page("Login");
else:
    if st.session_state["Type"]=="Admin":
        #so to add the books first add the screen data 
        st.subheader("Add a New Book")
        #gethe details from the form/data presentation layer;
        book_name = st.text_input("Book Name", "")
        book_author = st.text_input("Book Author", "")
        published_year = st.number_input("Published Year", min_value=1000, max_value=9999, step=1)
        quantity = st.number_input("Quantity", min_value=0, step=1)

        if st.button("Add Book"):
            if book_name and book_author and published_year and quantity is not None:
                res = Book.create_book(st.session_state["conn"],st.session_state["cursor"],book_name, book_author, published_year, quantity)
                st.success(res);
        
            else:
                st.error("please enter the valid details");
    else:
        st.info("books can be added only by adminstrators. sry access denied.");
        