from datetime import date;

def reserve_book(con, cursor, student_id, book_id, status='reserved'):
    reservation_date = date.today()  # Assuming today's date for the reservation
    
    # Check if there are enough available books before making a reservation
    check_quantity_sql = "SELECT quantity FROM Book WHERE book_id = ?"
    cursor.execute(check_quantity_sql, (book_id,))
    current_quantity = cursor.fetchone()

    if current_quantity and current_quantity[0] > 0:
        # Reduce the quantity in the Book table
        update_quantity_sql = "UPDATE Book SET quantity = quantity - 1 WHERE book_id = ?"
        cursor.execute(update_quantity_sql, (book_id,))
        con.commit()

        # Make the reservation
        insert_reservation_sql = "INSERT INTO BookReservation (student_id, book_id, reservation_date, status) VALUES (?, ?, ?, ?)"
        values = (student_id, book_id, reservation_date, status)
        cursor.execute(insert_reservation_sql, values)
        con.commit()

        return "Book reserved successfully!";
    else:
        return "Book not available for reservation.";


def book_returned(conn,cursor,student_id, book_id):
    update_query = "UPDATE BookReservation SET status = 'returned' WHERE student_id = ? AND book_id = ? AND status = 'reserved'"
    cursor.execute(update_query, (student_id, book_id))

    # Commit the changes
    conn.commit();
    return "Book status updated successfully"

