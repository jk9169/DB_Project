import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
DATABASE = 'database/event_booking.db'

# Database connection function
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    return conn

# Event list route
@app.route('/events', methods=['GET'])
def events():
    conn = get_db_connection()
    events = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    return render_template('events.html', events=events)

# Search route - based on location
@app.route('/search_by_location', methods=['GET'])
def search_by_location():
    location = request.args.get('location')  # Location entered by the user
    conn = get_db_connection()
    
    # Search events based on location
    events = conn.execute('SELECT * FROM events WHERE location LIKE ?', ('%' + location + '%',)).fetchall()
    conn.close()
    
    return render_template('events.html', events=events, location=location)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
