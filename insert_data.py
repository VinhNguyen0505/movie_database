import sqlite3
import csv

conn = sqlite3.connect('movie_database.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Movies (
    MovieID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    ReleaseYear INTEGER,
    Genre TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Directors (
    DirectorID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Actors (
    ActorID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS MovieActors (
    MovieID INTEGER,
    ActorID INTEGER,
    ActorName TEXT,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID),
    PRIMARY KEY (MovieID, ActorID)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Reviews (
    ReviewID INTEGER PRIMARY KEY,
    MovieID INTEGER,
    Rating FLOAT CHECK (Rating >= 0 AND Rating <= 5),
    ReviewText TEXT,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
);
""")

with open('movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
 
    cursor.executemany("INSERT INTO Movies (MovieID, Title, ReleaseYear, Genre) VALUES (?, ?, ?, ? )", reader)
 
with open('actors.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    cursor.executemany("INSERT INTO Actors (ActorID, Name) VALUES (?, ?)", reader)
    
with open('directors.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    cursor.executemany("INSERT INTO Directors (DirectorID, Name) VALUES (?, ?)", reader)
     
 
conn.commit()
print("Movies inserted successfully!")
conn.close()