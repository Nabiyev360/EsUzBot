import sqlite3


path_to_db = 'data/main.db'
path_to_words = 'data/words.db'


def create_table():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER,
            full_name TEXT,
            username TEXT
        )""")
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS channels (
            channel_id INTEGER,
            channel_name TEXT,
            channel_username TEXT
        )""")
    conn.commit()
    conn.close()


# Create table words
    conn = sqlite3.connect(path_to_words)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS words (
            word_id INTEGER PRIMARY KEY AUTOINCREMENT,
            eng TEXT,
            uz TEXT
        )""")
    conn.commit()
    conn.close()



def add_user(user_id, fullname, username = None):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
    if not c.fetchone():
        new_data = (user_id, fullname, username)
        c.execute(f"INSERT INTO users VALUES (?,?,?)", new_data)
        conn.commit()
    conn.close()

def add_channel(channel_id, channel_name, channel_username = None):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    new_data = (channel_id, channel_name, channel_username)
    c.execute(f"INSERT INTO channels VALUES (?,?,?)", new_data)
    conn.commit()
    conn.close()

def delete_channel(channel_username):
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"DELETE FROM channels WHERE channel_username = '{channel_username}'")
    conn.commit()
    conn.close()

def get_users_id():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT user_id FROM users")
    sender_id = c.fetchall()
    return sender_id
    
def get_channels():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT * FROM channels")
    channels = c.fetchall()
    return channels

def count_users():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT COUNT() FROM users")
    count = c.fetchone()[0]
    return count
    
def count_group():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    c.execute(f"SELECT user_id FROM users WHERE user_id LIKE '-%'")
    count = len(c.fetchall())
    return count
    
    
# def tr_count():
#     conn = sqlite3.connect(path_to_db)
#     c = conn.cursor()
#     c.execute(f"SELECT td_count FROM bot_stat")
#     count = c.fetchone()
#     print(count)
#     return count
    
    
def td_update():
    conn = sqlite3.connect(path_to_db)
    c = conn.cursor()
    
    c.execute(f"SELECT td_count FROM bot_stat")
    after_count = c.fetchone()[0]

    c.execute(
        f"UPDATE bot_stat SET td_count = {after_count+1} WHERE td_count = {after_count}"
        )
    conn.commit()
        
    c.execute(f"SELECT td_count FROM bot_stat")
    count = c.fetchone()[0]
    return count

def get_trans(eng_word):
    conn = sqlite3.connect(path_to_words)
    c = conn.cursor()
    c.execute(f"SELECT uz FROM words WHERE eng=?", (eng_word,))
    # c.execute(f"SELECT uz FROM words WHERE eng = '{eng_word}'")
    uz = c.fetchall()
    return uz