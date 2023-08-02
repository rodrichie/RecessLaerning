#1a) Show a context manager for file handling that automatically opens and closes a file.

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Using the context manager
with open_file("example_file.txt", "w") as file:
    file.write("Hello, World!")




#b) Shows a context manager for managing a database connection.
import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(db_name):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()

# Using the context manager
with db_connection("mydatabase.db") as conn:
    cursor = conn.cursor()
    
    # Create the "users" table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    
    # Insert some sample data into the "users" table
    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    
    # Retrieve data from the "users" table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



#c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.


import threading
import time
import multiprocessing

def function(seconds):
    time.sleep(seconds)
    print('Function ran for {} seconds'.format(seconds))

if __name__ == '__main__':
    threads = []
    processes = []
    for i in range(3):
        thread = threading.Thread(target=function, args=[i*2])
        threads.append(thread)
        process = multiprocessing.Process(target=function, args=[i*2])
        processes.append(process)

    for thread in threads:
        thread.start()

    for process in processes:
        process.start()

    for thread in threads:
        thread.join()

    for process in processes:
        process.join()

