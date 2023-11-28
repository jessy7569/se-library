#create the insert operation for the book 
from datetime import date;

def insert_report_data(conn,cursor,student_id, lib_id, report_description, report_date):
    query = "INSERT INTO Report (Student_ID, Lib_id, report_description, report_date) VALUES (?, ?, ?, ?)"
    values = (student_id, lib_id, report_description, report_date)
    
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    

# Function to check if a report exists for the specified Student_ID
def check_report_existence(conn,cursor,student_id):
    cursor = conn.cursor()
    print("inside the report existence")
    cursor.execute("SELECT COUNT(*) FROM Report WHERE Student_ID = ?", (student_id,));
    return cursor.fetchone()[0] > 0
