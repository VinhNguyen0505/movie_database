import sqlite3
import csv

conn = sqlite3.connect('movie_database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS MovieActors (
    MovieID INTEGER,
    ActorID INTEGER,
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID),
    PRIMARY KEY (MovieID, ActorID)
    );
""")

with open('movie_actors.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    
    cursor.executemany("INSERT INTO MovieActors (MovieID, ActorID) VALUES (?, ?)", reader)
    
conn.commit()
print("Task Completed!")
conn.close()