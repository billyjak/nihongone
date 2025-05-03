import sqlite3
from .kanji import Kanji  # Assuming your Kanji class is in a separate module named kanji

class KanjiManager:
    def __init__(self, db_path='/home/williamg/code/python/nihongone/data/kanji_project.db'):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()


    def filter_kanji(self, **filters):
        query = "SELECT * FROM kanji WHERE 1=1"
        params = []
        
        # Handle normal filters first
        for key, value in filters.items():
            if key == 'meanings' and value is not None:
                # Use a subquery to filter by meanings, case-insensitive
                query += " AND kanji_id IN (SELECT kanji_id FROM meanings WHERE LOWER(meaning) = ?)"
                params.append(value.lower())
            elif key == 'readings_on' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM readings_on WHERE LOWER(reading_on) = ?)"
                params.append(value.lower())
            elif key == 'readings_kun' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM readings_kun WHERE LOWER(reading_kun) = ?)"
                params.append(value.lower())
            elif key == 'wk_meanings' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM wk_meanings WHERE LOWER(wk_meaning) = ?)"
                params.append(value.lower())
            elif key == 'wk_readings_on' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM wk_readings_on WHERE LOWER(wk_reading_on) = ?)"
                params.append(value.lower())
            elif key == 'wk_readings_kun' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM wk_readings_kun WHERE LOWER(wk_reading_kun) = ?)"
                params.append(value.lower())
            elif key == 'wk_radicals' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM wk_radicals WHERE LOWER(wk_radical) = ?)"
                params.append(value.lower())
            elif key == 'examples' and value is not None:
                query += " AND kanji_id IN (SELECT kanji_id FROM examples WHERE LOWER(example) = ?)"
                params.append(value.lower())
            elif value is not None:
                # Normal filter for columns in the main kanji table
                query += f" AND {key} = ?"
                params.append(value)
        
        query += " ORDER BY jlpt_new ASC, freq IS NULL, freq ASC"
        self.cursor.execute(query, params)
        kanji_rows = self.cursor.fetchall()
        return [self._build_kanji_object(row, row[0]) for row in kanji_rows]


    def get_unknown_kanji_by_jlpt(self):
        query = """
        SELECT * FROM kanji 
        WHERE learned = FALSE AND jlpt_new IS NOT NULL
        ORDER BY jlpt_new ASC, freq IS NULL, freq ASC
        """
        self.cursor.execute(query)
        kanji_rows = self.cursor.fetchall()
        return [self._build_kanji_object(row, row[0]) for row in kanji_rows]

    def mock_kanji(self):
        test_kanji = Kanji("test", 1, 2, 3, 4, 5, ["meanings test 1", "meanings test 2"], ["readings_on test 1", "readings_on test 2"], ["readings_kun test 1", "readings_kun test 2"], 6, ["wk_meanings test 1", "wk_meanings test 2"], ["wk_readings_on test 1", "wk_readings_on test 2"], ["wk_readings_kun test 1", "wk_readings_kun test 2"], ["wk_radicals test 1", "wk_radicals test 2"], ["examples test 1", "examples test 2"])
        return test_kanji


    def get_one_kanji(self):
        query = """
        SELECT *
        FROM kanji
        ORDER BY RANDOM() LIMIT 1
        """
        self.cursor.execute(query)
        row = self.cursor.fetchone()
        if row:
            kanji_id = row[0]
            return self._build_kanji_object(row, kanji_id)
        return None


    def get_ten_kanji(self):
        query = """
        SELECT *
        FROM kanji
        ORDER BY RANDOM() LIMIT 10
        """
        self.cursor.execute(query)
        kanji_rows = self.cursor.fetchall()
        return [self._build_kanji_object(row, row[0]) for row in kanji_rows]


    def _get_related_data(self, table_name, kanji_id):
        query = f"SELECT * FROM {table_name} WHERE kanji_id = ?"
        self.cursor.execute(query, (kanji_id,))
        rows = self.cursor.fetchall()
        return [row[2] for row in rows] if rows else []

    def add_example(self, kanji_id, example):
        query = "INSERT INTO examples (kanji_id, example) VALUES (?, ?)"
        self.cursor.execute(query, (kanji_id, example))
        self.connection.commit()

    def update_example(self, example_id, new_example):
        query = "UPDATE examples SET example = ? WHERE example_id = ?"
        self.cursor.execute(query, (new_example, example_id))
        self.connection.commit()

    def delete_example(self, example_id):
        query = "DELETE FROM examples WHERE example_id = ?"
        self.cursor.execute(query, (example_id,))
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

    def _build_kanji_object(self, row, kanji_id):
        meanings = self._get_related_data('meanings', kanji_id)
        readings_on = self._get_related_data('readings_on', kanji_id)
        readings_kun = self._get_related_data('readings_kun', kanji_id)
        wk_meanings = self._get_related_data('wk_meanings', kanji_id)
        wk_readings_on = self._get_related_data('wk_readings_on', kanji_id)
        wk_readings_kun = self._get_related_data('wk_readings_kun', kanji_id)
        wk_radicals = self._get_related_data('wk_radicals', kanji_id)
        examples = self._get_related_data('examples', kanji_id)

        return Kanji(
            kanji=row[1],
            strokes=row[2],
            grade=row[3],
            freq=row[4],
            jlpt_old=row[5],
            jlpt_new=row[6],
            meanings=meanings,
            readings_on=readings_on,
            readings_kun=readings_kun,
            wk_level=row[7],
            wk_meanings=wk_meanings,
            wk_readings_on=wk_readings_on,
            wk_readings_kun=wk_readings_kun,
            wk_radicals=wk_radicals,
            examples=examples
        )

# Example usage
if __name__ == "__main__":
    manager = KanjiManager()
    
    def is_sorted_by_jlpt_and_freq(jlpt_kanji):
        for i in range(1, len(jlpt_kanji)):
            current = jlpt_kanji[i]
            previous = jlpt_kanji[i - 1]
            
            # Handle `None` in jlpt_new
            if current.jlpt_new is None or previous.jlpt_new is None:
                raise ValueError("jlpt_new cannot be None. Check the data source.")
            
            # Compare JLPT level
            if current.jlpt_new < previous.jlpt_new:
                return False
            
            # If JLPT level is the same, compare frequency
            if current.jlpt_new == previous.jlpt_new:
                prev_freq = previous.freq
                curr_freq = current.freq
                
                # Handle NULL frequencies (None in Python)
                if prev_freq is None and curr_freq is not None:
                    continue  # Correct: None should come before any number
                if prev_freq is not None and curr_freq is None:
                    return False  # Incorrect: A number should not come before None
                if prev_freq is not None and curr_freq is not None and curr_freq < prev_freq:
                    return False  # Incorrect: Frequency is not sorted in ascending order
        return True

    # Testing the method
    jlpt_kanji = manager.get_unknown_kanji_by_jlpt()
    if is_sorted_by_jlpt_and_freq(jlpt_kanji):
        print("Sorting is correct!")
    else:
        print("Sorting is incorrect!")


    #
    # # Filtering kanji by multiple attributes
    # filtered_kanji = manager.filter_kanji(grade=1, jlpt_new=5)
    # print("Filtered Kanji by Grade 1 and JLPT 5:", filtered_kanji)
    #
    # # Get unknown kanji by JLPT level
    # unknown_kanji = manager.get_unknown_kanji_by_jlpt()
    # print("Unknown Kanji by JLPT level:", unknown_kanji)
    #
    # # Add a new example
    # manager.add_example(kanji_id=1, example="This is an example sentence.")
    #
    # # Update an example
    # manager.update_example(example_id=1, new_example="Updated example sentence.")
    #
    # # Delete an example
    # manager.delete_example(example_id=1)
    #
    # # Close the connection
    # manager.close_connection()
    #
