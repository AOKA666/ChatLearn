import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('conversation.db', check_same_thread=False)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS conversation
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                             role TEXT,
                             content TEXT);''')
        self.conn.commit()

    def add_conversation(self, role, content):
        self.conn.execute("INSERT INTO conversation (role, content) VALUES (?, ?)", (role, content))
        self.conn.commit()

    def get_conversation(self):
        rows = self.conn.execute("SELECT * FROM conversation").fetchall()
        conversation = [{'role': row[1], 'content': row[2]} for row in rows]
        return conversation

    def close_connection(self):
        self.conn.close()