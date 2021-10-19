DROP TABLE IF EXISTS user;


CREATE TABLE user (
    id INTEGER PRIMARY KEY autoincrement,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
