import mysql.connector

class User:
    def __init__(self, host, user, password, database):
        """
        Initializes the database connection.
        """
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_user(self, username, email, password):
        """
        Creates a new user in the database.
        """
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        values = (username, email, password)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user(self, username, password):
        """
        Retrieves a user by username and password.
        """
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, password))
        return self.cursor.fetchone()

    def update_user(self, user_id, new_username):
        """
        Updates the username of an existing user.
        """
        query = "UPDATE users SET username = %s WHERE id = %s"
        values = (new_username, user_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount

    def delete_user(self, user_id):
        """
        Deletes a user by ID.
        """
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
        return self.cursor.rowcount
