import sqlite3

conn = sqlite3.connect('database/event_booking.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
for r in rows:
    print(r)

conn.close()
