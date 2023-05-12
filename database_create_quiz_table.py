import sqlite3

# Connect to the database
conn = sqlite3.connect('quizdb.db')

# Create a cursor object to interact with the database
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE quiz
             (id INTEGER PRIMARY KEY,
              name TEXT NOT NULL,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# Save the changes
conn.commit()

# Close the connection
conn.close()