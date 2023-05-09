import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('conversation.db',check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS conversation
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             role TEXT,
                             content TEXT);''')
        self.conn.commit()

    def add_conversation(self, role, content):
        self.cur.execute("INSERT INTO conversation (role, content) VALUES (?, ?)", (role, content))
        self.conn.commit()

    def get_conversation(self):
        self.cur.execute("SELECT * FROM conversation")
        rows = self.cur.fetchall()
        conversation = [{'role': row[1], 'content': row[2]} for row in rows]
        return conversation

    def close_connection(self):
        self.conn.close()