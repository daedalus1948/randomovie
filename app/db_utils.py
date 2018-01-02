import sqlite3

def set_DB_PATH(path):
    global DB_PATH
    if type(path) != str:
        print("please supply a correct path")
    else:
        DB_PATH = path
        print("Path has been set!")

def per_request_connection_select_query(query):  # project specific only select query
    try:
        conn = sqlite3.connect(DB_PATH)
        try:
            c = conn.cursor()
            c.execute(query)
            data = c.fetchone()
            return data
        except Exception as e:
            print(str(e))
        finally:
            conn.close()
    except Exception as e:
        print(str(e))
    else:
        print("everything worked fine!")


def build_dict(db_query):  # project specific
    return {"name":db_query[0], "year":db_query[1], "url":db_query[2]}


# the filepath string locating the database file(s)
DB_PATH = ""

# predefined raw queries
SCIFI = "SELECT name, year, url, type FROM movies JOIN movies_genres as mg ON movies.ID = mg.ID_movie JOIN genres ON genres.ID = mg.ID_genre WHERE type='scifi' ORDER BY Random() LIMIT 1;"
ACTION = "SELECT name, year, url, type FROM movies JOIN movies_genres as mg ON movies.ID = mg.ID_movie JOIN genres ON genres.ID = mg.ID_genre WHERE type='action' ORDER BY Random() LIMIT 1;"
DRAMA = "SELECT name, year, url, type FROM movies JOIN movies_genres as mg ON movies.ID = mg.ID_movie JOIN genres ON genres.ID = mg.ID_genre WHERE type='drama' ORDER BY Random() LIMIT 1;"
COMEDY = "SELECT name, year, url, type FROM movies JOIN movies_genres as mg ON movies.ID = mg.ID_movie JOIN genres ON genres.ID = mg.ID_genre WHERE type='comedy' ORDER BY Random() LIMIT 1;"
HORROR = "SELECT name, year, url, type FROM movies JOIN movies_genres as mg ON movies.ID = mg.ID_movie JOIN genres ON genres.ID = mg.ID_genre WHERE type='horror' ORDER BY Random() LIMIT 1;"
