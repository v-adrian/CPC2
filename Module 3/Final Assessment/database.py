import sqlite3


def save_score(name, score, time):
    conn = sqlite3.connect('player_scores.db')
    c = conn.cursor()

    if len(name) > 1:
        c.execute(
            f'''INSERT INTO scores(player_name, player_score, player_time) VALUES (
                "{name}", 
                "{score}", 
                "{time}"
                ) 
                ON CONFLICT(player_name) DO UPDATE SET
                player_score=excluded.player_score,
                player_time=excluded.player_time 
                WHERE excluded.player_time<scores.player_time;
             ''')

    conn.commit()
    conn.close()


def show_scores():
    conn = sqlite3.connect('player_scores.db')
    c = conn.cursor()

    leaderboards = dict()
    try:
        c.execute('''SELECT * FROM scores''')
        data = c.fetchall()
        for name, tries, time in data:
            if name not in leaderboards:
                leaderboards[name] = list()
            leaderboards[name].extend([tries, time])
    except:
        return leaderboards

    conn.commit()
    conn.close()
    return leaderboards


def create_table():
    conn = sqlite3.connect('player_scores.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS scores(
        player_name text UNIQUE,
        player_score INTEGER,
        player_time INTEGER
    )''')

    conn.commit()
    conn.close()


def remove_scores():
    conn = sqlite3.connect('player_scores.db')
    c = conn.cursor()

    c.execute('''DROP TABLE scores''')

    conn.commit()
    conn.close()
