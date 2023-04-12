-- Create the 'authors' table
CREATE TABLE authors (author_id INTEGER PRIMARY KEY, name TEXT);
.separator ,
.import --skip 1 csv/authors.csv authors

-- Create the 'genres' table
CREATE TABLE genres (genre_id INTEGER PRIMARY KEY, name TEXT);
.separator ,
.import --skip 1 csv/genres.csv genres

-- Create the 'start_dates' table
CREATE TABLE start_dates (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week TEXT,
    day_of_year INTEGER
);
.separator ,
.import --skip 1 csv/start_dates.csv start_dates

-- Create the 'items' table
CREATE TABLE items (item_id INTEGER PRIMARY KEY, title TEXT, year INTEGER);
.separator ,
.import --skip 1 csv/items_clean.csv items

-- Create the 'users' table
CREATE TABLE users (user_id INTEGER PRIMARY KEY, age_group TEXT, age INTEGER, sex TEXT);
.separator ,
.import --skip 1 csv/users_new.csv users

-- Create the 'interactions' table
CREATE TABLE interactions (
    user_id INTEGER,
    item_id INTEGER,
    start_date_id INTEGER,
    progress INTEGER,
    rating INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (item_id) REFERENCES items_clean(id),
    FOREIGN KEY (start_date_id) REFERENCES start_dates(date_id)
);
.separator ,
.import --skip 1 csv/interactions_new.csv interactions

-- Create the 'items_authors' table
CREATE TABLE items_authors (
    item_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (author_id) REFERENCES authors(id)
);
.separator ,
.import --skip 1 csv/items_authors.csv items_authors

-- Create the 'items_genres' table
CREATE TABLE items_genres (
    item_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (item_id) REFERENCES items(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);
.separator ,
.import --skip 1 csv/items_genres.csv items_genres
