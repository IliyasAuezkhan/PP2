import psycopg2
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

def init_db():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS players (
            id       SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS game_sessions (
            id            SERIAL PRIMARY KEY,
            player_id     INTEGER REFERENCES players(id),
            score         INTEGER   NOT NULL,
            level_reached INTEGER   NOT NULL,
            played_at     TIMESTAMP DEFAULT NOW()
        );
        """
    )
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error initializing DB: {error}")
    finally:
        if conn is not None:
            conn.close()

def save_result(username, score, level_reached):
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        
        cur.execute(
            "INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING;",
            (username,)
        )
        cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
        player_id = cur.fetchone()[0]
        
        
        cur.execute(
            "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);",
            (player_id, score, level_reached)
        )
        
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error saving results: {error}")
    finally:
        if conn is not None:
            conn.close()

def get_top_scores(limit=10):
    conn = None
    results = []
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, s.score, s.level_reached, s.played_at 
            FROM game_sessions s
            JOIN players p ON s.player_id = p.id
            ORDER BY s.score DESC
            LIMIT %s;
        """, (limit,))
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error fetching leaderboard: {error}")
    finally:
        if conn is not None:
            conn.close()
    return results

def get_personal_best(username):
    conn = None
    best_score = 0
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT MAX(s.score) 
            FROM game_sessions s
            JOIN players p ON s.player_id = p.id
            WHERE p.username = %s;
        """, (username,))
        row = cur.fetchone()
        if row and row[0]:
            best_score = row[0]
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error fetching personal best: {error}")
    finally:
        if conn is not None:
            conn.close()
    return best_score
