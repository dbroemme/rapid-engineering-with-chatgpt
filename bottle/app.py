# app.py
from bottle import Bottle, run, template
from bottle.ext import sqlite

# Create a Bottle app instance
app = Bottle()
plugin = sqlite.Plugin(dbfile='../helloworld/db.sqlite3')
app.install(plugin)

@app.route('/')
@app.route('/quizzes')
def quiz_list(db):
    # Query the database for the list of quizzes
    cursor = db.execute('SELECT name FROM helloworldapp_quiz')
    quizzes = [row[0] for row in cursor.fetchall()]

    # Render the template with the quiz list data
    return template('quiz_list', quizzes=quizzes)

# Run the Bottle app
if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
