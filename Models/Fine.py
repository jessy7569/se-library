# Function to insert fine data into the Fines table
def insert_fine_data(conn,book_returned, deadline, fine_amount, student_id,book_id, lib_id):
    query = "INSERT INTO Fines (book_returned, deadline, fine_amount, student_id,book_id, lib_id) VALUES (?, ?, ?, ?, ?,?)"
    values = (book_returned, deadline, fine_amount, student_id, book_id,lib_id)
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit();

def fetch_student_fines(conn,student_id):
    cursor = conn.cursor()
    query = """
    SELECT F.fine_id, F.book_returned, F.deadline, F.fine_amount, B.book_name, F.lib_id
    FROM Fines F JOIN Book B ON F.book_id = B.book_id
    WHERE F.student_id = ?
    """
    cursor.execute(query, (student_id,))
    fines = cursor.fetchall()
    return fines