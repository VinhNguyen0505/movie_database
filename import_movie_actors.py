import sqlite3
import csv

conn = sqlite3.connect('movie_database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Movies(
    MovieID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL,
    ReleaseYear INTEGER,
    Genre TEXT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Actors(
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

with open('movie_actors.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)

    data_to_insert = []
    for row in reader:
        movie_id, actor_id = row
        cursor.execute("SELECT Name FROM Actors WHERE ActorID = ?", (actor_id,))
        actor_name = cursor.fetchone()
        if actor_name:
            data_to_insert.append((movie_id, actor_id, actor_name[0]))
    
    cursor.executemany("INSERT OR IGNORE INTO MovieActors (MovieID, ActorID, ActorName) VALUES (?, ?, ?)", data_to_insert)
    
conn.commit()
print("Task Completed!")
conn.close()