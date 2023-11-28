#create a book class and provide all the curd operations
from datetime import date;
import streamlit as st;
def create_book(con , cursor, book_name, book_author, published_year, quantity):
    sql = "INSERT INTO book (book_name, book_author, published_year, quantity) VALUES (?, ?, ?, ?)"
    values = (book_name, book_author, published_year, quantity)
    cursor.execute(sql, values)
    con.commit()
    return ("Book added successfully!")

# Read
def read_books(cursor):
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    books = cursor.fetchall()
    return books;


def search_books(name=None, author=None, published_year=None):
    query = "SELECT * FROM Book WHERE 1=1"
    parameters = []

    if name:
        query += " AND book_name LIKE ?"
        parameters.append(f"%{name}%")
    if author:
        query += " AND book_author LIKE ?"
        parameters.append(f"%{author}%")
    if published_year:
        query += " AND published_year = ?"
        parameters.append(published_year)
    cursor = st.session_state["cursor"];
    cursor.execute(query, parameters)
    return cursor.fetchall()

def fetch_available_books(con):
    cursor = con.cursor()
    cursor.execute("SELECT book_id, book_name FROM Book WHERE quantity > 0")
    books = cursor.fetchall()
    return [(book_name, book_id) for book_id, book_name in books];

def fetch_books_by_student(con,student_id):
    cursor = con.cursor()
    query = "SELECT book_id, book_name FROM Book WHERE book_id IN (SELECT book_id FROM BookReservation WHERE student_id = ? and status = 'reserved')"
    cursor.execute(query, (student_id,))
    books = cursor.fetchall()
    return [(book_name, book_id) for book_id, book_name in books];
