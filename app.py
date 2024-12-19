import sqlite3
from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/users', methods=['GET'])
def users():
    conn = get_db_connection()
    users = conn.execute ('SELECT username, email FROM users').fetchall()
    conn.close
    return render_template('users.html', users = users)

# Add new event route
@app.route('/add_event', methods=['POST'])
def add_event():
    # Get form data
    event_name = request.form['event_name']
    event_date = request.form['event_date']
    location = request.form['location']
    
    # Insert data into the database
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO events (event_name, event_date, location) VALUES (?, ?, ?)',
        (event_name, event_date, location)
    )
    conn.commit()
    conn.close()
    
    # Redirect to home after adding the event
    return redirect(url_for('home'))

# Search route - based on location
@app.route('/search_by_location', methods=['GET']) 
def search_by_location():
    location = request.args.get('location')  # Location entered by the user
    conn = get_db_connection()
    
    # Search events based on location
    events = conn.execute('SELECT event_name, event_date, location, ticket_count FROM events INNER JOIN tickets USING (event_id) WHERE location LIKE ?', ('%' + location + '%',)).fetchall()
    conn.close()
    
    return render_template('events.html', events=events, location=location)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
