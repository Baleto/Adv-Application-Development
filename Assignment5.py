#Program Name: Assignment5.py
#Course: IT3883/Section 01
#Student Name: Benel Kawata
#Assignment Number: Assignment 5
#Due Date: [Enter the due date]
#Purpose: The program aims to store temperature readings within a SQLite database
#it uses SQL to determine the Sunday and Thursday averages temperature.
#Resources: Assignment 5 instructions and the supplied input file; w3schools. 

import sqlite3 #Here, an import statement is used to include the sqlite3 module, providing the necessary functions and classes for creating and managing SQLite databases in Python.
from pathlib import Path #Additionally, the pathlib module is imported to handle file paths in a platform-independent way.

def main():
    #In this block of code, both files are located beside this Python program.
    folder = Path(__file__).resolve().parent
    in_path = folder / "Assignment5input(1).txt" #There was a bit of laziness in naming the input file, but it is still readable.
    db_path = folder / "temperatures.db"

    #On this specific line, connecting creates the database if it does not exist.
    conn = sqlite3.connect(db_path)
    try:
        #In this block of code, changes are committed together or rolled back on error.
        with conn:
            cur = conn.cursor()

            #In this block of code, the table contains the three required fields.
            #SQLite uses TEXT for strings and REAL for floating-point values.
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Temperatures (
                    ID INTEGER PRIMARY KEY,
                    Day_Of_Week TEXT,
                    Temperature_Value REAL
                )
            """)

            #On this specific line, old readings are removed to prevent duplicate imports.
            cur.execute("DELETE FROM Temperatures")

            #In this block of code, each nonempty line supplies a day and temperature.
            with in_path.open("r") as in_file:
                for ln in in_file:
                    if not ln.strip():
                        continue
                    day, temp = ln.split()

                    #On this specific line, placeholders pass values safely into SQL.
                    #SQLite assigns the integer primary key automatically.
                    cur.execute(
                        "INSERT INTO Temperatures "
                        "(Day_Of_Week, Temperature_Value) VALUES (?, ?)",
                        (day, float(temp))
                    )

            #In this block of code, SQL calculates each requested day's average.
            for day in ("Sunday", "Thursday"):
                cur.execute(
                    "SELECT AVG(Temperature_Value) FROM Temperatures "
                    "WHERE Day_Of_Week = ?",
                    (day,)
                )
                avg = cur.fetchone()[0]
                if avg is None:
                    print(f"{day}: No temperature readings found.")
                else:
                    print(f"Average temperature for {day}: {avg:.2f}")
    finally:
        #On this specific line, the connection closes even if an error occurs.
        conn.close()

if __name__ == "__main__":
    main()

