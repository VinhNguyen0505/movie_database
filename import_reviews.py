import sqlite3
import csv

conn = sqlite3.connect("movie_database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Reviews (
    ReviewID INTEGER PRIMARY KEY,
    MovieID INTEGER,
    Rating FLOAT CHECK (Rating >= 0 AND Rating <= 5),
    ReviewText TEXT,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
);
""")

with open("reviews.csv", 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    cursor.executemany("INSERT INTO Reviews(ReviewID, MovieID, Rating, ReviewText) VALUES(?, ?, ?, ?)",reader)

conn.commit()
print("Task Completed!")
conn.close()