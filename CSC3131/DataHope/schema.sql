--Creates a table called user

DROP TABLE IF EXISTS user;


CREATE TABLE user (
    id INTEGER PRIMARY KEY autoincrement,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    charity TEXT NOT NULL,
    email TEXT NOT NULL
);
