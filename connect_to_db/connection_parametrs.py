import sqlite3;

def connection():
    #my sql connector to db; 
    
#    conn = mysql.connector.connect(host="localhost",user="root",password="Vikram@9999",database="Library");
    conn = sqlite3.connect('pages/Library.db')
    cur = conn.cursor();
    return conn,cur;

    
