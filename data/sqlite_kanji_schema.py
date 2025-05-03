import sqlite3
import json

# Load your JSON data
with open('/home/williamg/code/python/nihongone/data/davidluzgouveia_kanji_database/kanjiapi_full.json', 'r', encoding='utf-8') as f:
    kanji_data = json.load(f)

# Connect to the SQLite database
connection = sqlite3.connect('kanji_project.db')
cursor = connection.cursor()

# Create the tables
sql_script = """
-- Main kanji table
CREATE TABLE kanji (
    kanji_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji TEXT UNIQUE NOT NULL,
    strokes INTEGER,
    grade INTEGER,
    freq INTEGER,
    jlpt_old INTEGER,
    jlpt_new INTEGER,
    wk_level INTEGER,
    learned BOOLEAN DEFAULT FALSE
);

-- Meanings table
CREATE TABLE meanings (
    meaning_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    meaning TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- Readings On table
CREATE TABLE readings_on (
    reading_on_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    reading_on TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- Readings Kun table
CREATE TABLE readings_kun (
    reading_kun_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    reading_kun TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- WK Meanings table
CREATE TABLE wk_meanings (
    wk_meaning_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    wk_meaning TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- WK Readings On table
CREATE TABLE wk_readings_on (
    wk_reading_on_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    wk_reading_on TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- WK Readings Kun table
CREATE TABLE wk_readings_kun (
    wk_reading_kun_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    wk_reading_kun TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- WK Radicals table
CREATE TABLE wk_radicals (
    wk_radical_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    wk_radical TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);

-- Examples table
CREATE TABLE examples (
    example_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    example TEXT,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);


-- Kanji Reviews table
CREATE TABLE kanji_reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    kanji_id INTEGER,
    review_stage INTEGER,
    learned_date DATE,
    next_review_date DATE,
    FOREIGN KEY (kanji_id) REFERENCES kanji (kanji_id)
);
"""
cursor.executescript(sql_script)

# Insert data into the tables
for kanji, details in kanji_data.items():
    # Insert into kanji table
    cursor.execute("""
        INSERT INTO kanji (kanji, strokes, grade, freq, jlpt_old, jlpt_new, wk_level)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        kanji,
        details.get("strokes"),
        details.get("grade"),
        details.get("freq"),
        details.get("jlpt_old"),
        details.get("jlpt_new"),
        details.get("wk_level")
    ))
    
    kanji_id = cursor.lastrowid

    # Insert into meanings table
    for meaning in details.get("meanings", []) or []:
        cursor.execute("""
            INSERT INTO meanings (kanji_id, meaning)
            VALUES (?, ?)
        """, (kanji_id, meaning))
    
    # Insert into readings_on table
    for reading_on in details.get("readings_on", []) or []:
        cursor.execute("""
            INSERT INTO readings_on (kanji_id, reading_on)
            VALUES (?, ?)
        """, (kanji_id, reading_on))

    # Insert into readings_kun table
    for reading_kun in details.get("readings_kun", []) or []:
        cursor.execute("""
            INSERT INTO readings_kun (kanji_id, reading_kun)
            VALUES (?, ?)
        """, (kanji_id, reading_kun))

    # Insert into wk_meanings table
    for wk_meaning in details.get("wk_meanings", []) or []:
        cursor.execute("""
            INSERT INTO wk_meanings (kanji_id, wk_meaning)
            VALUES (?, ?)
        """, (kanji_id, wk_meaning))

    # Insert into wk_readings_on table
    for wk_reading_on in details.get("wk_readings_on", []) or []:
        cursor.execute("""
            INSERT INTO wk_readings_on (kanji_id, wk_reading_on)
            VALUES (?, ?)
        """, (kanji_id, wk_reading_on))

    # Insert into wk_readings_kun table
    for wk_reading_kun in details.get("wk_readings_kun", []) or []:
        cursor.execute("""
            INSERT INTO wk_readings_kun (kanji_id, wk_reading_kun)
            VALUES (?, ?)
        """, (kanji_id, wk_reading_kun))

    # Insert into wk_radicals table
    for wk_radical in details.get("wk_radicals", []) or []:
        cursor.execute("""
            INSERT INTO wk_radicals (kanji_id, wk_radical)
            VALUES (?, ?)
        """, (kanji_id, wk_radical))

# Commit changes and close the connection
connection.commit()
connection.close()

