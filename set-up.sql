CREATE TABLE events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date DATE NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    user_id INTEGER,
    ticket_count INTEGER NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events (event_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

INSERT INTO events (event_id, event_name, event_date, location)
VALUES 
(8, "Eras", "2024-12-18", "Bridgewater"), 
(9, "Bruins", "2024-12-12", "TDGarden");

INSERT INTO users (user_id, username, email)
VALUES 
(1, "someone123", "someone123@gmail.com"), 
(2, "dasher87", "dasher87@gmail.com");

INSERT INTO tickets (ticket_id, event_id, user_id, ticket_count)
VALUES 
(1, 6, 2, 3), 
(2, 9, 1, 4);
