import sqlite3

class User:
    def __init__(self, db_path="users.db"):
        """
        Initializes the database connection and creates the users table if it doesn't exist.
        """
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """
        Creates the users table if it does not already exist.
        """
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def create_user(self, username, email, password):
        """
        Creates a new user in the database.
        """
        query = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)"
        values = (username, email, password)
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # Username or email already exists

    def get_user(self, username, password):
        """Retrieves a user by username and password."""
        query = "SELECT id, username, email FROM users WHERE username = ? AND password = ?"
        try:
            self.cursor.execute(query, (username, password))
            return self.cursor.fetchone()
        except Exception as e:
            print("SQL Error:", e)  # Debugging
            return None
        
    def update_user(self, user_id, new_username):
        """
        Updates the username of an existing user.
        """
        query = "UPDATE users SET username = ? WHERE id = ?"
        values = (new_username, user_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount

    def delete_user(self, user_id):
        """
        Deletes a user by ID.
        """
        query = "DELETE FROM users WHERE id = ?"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
        return self.cursor.rowcount

    def close_connection(self):
        """ Closes the database connection. """
        self.conn.close()
