#this is avaibale for both admins and users as well.

#this access to all everyone.
from Models import Book;
import streamlit as st;
from streamlit_extras.switch_page_button import switch_page
import pandas as pd;
st.subheader("Search for Books")

name_filter = st.text_input("Book Name", "")
author_filter = st.text_input("Book Author", "")
published_year_filter = st.number_input("Published Year",max_value=9999, step=5)

if st.button("Search"):
    result = Book.search_books(name_filter, author_filter, published_year_filter)
    if not result:
        st.warning("No matching books found.")
    else:
        st.subheader("Search Results")
        search_results_df = pd.DataFrame(result, columns=["book_id", "book_name", "book_author", "published_year", "quantity"])
        st.write(search_results_df);

