import mysql.connector
import config as cfg

class part_DAO:
    def __init__(self):
        # Initialize part_DAO with database connection details from config
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None

    def getcursor(self):
        # Establish a database connection and return a cursor
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return self.connection.cursor()

    def close_all(self):
        # Close the database connection if it exists
        if self.connection:
            self.connection.close()

    def create(self, values):
        # Create a new record in the 'part' table
        with self.getcursor() as cursor:
            try:
                sql = "INSERT INTO part (Part_Name, Part_No, Price) VALUES (%s, %s, %s)"
                print("Debug: Values before execution:", values)
                cursor.execute(sql, tuple(values))
                self.connection.commit()
                new_id = cursor.lastrowid
            except Exception as e:
                print(f"Error in create: {e}")
                new_id = None
            cursor.close()
        return new_id

    def getAll(self):
        # Retrieve all records from the 'part' table
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM part"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [self.convert_to_dictionary(result) for result in results]
        finally:
            cursor.close()

    def find_by_id(self, _id):
        # Retrieve a record from the 'part' table by its ID
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM part WHERE id = %s"
            values = (_id,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convert_to_dictionary(result) if result else None
        finally:
            cursor.close()

    def update(self, values):
        # Update a record in the 'part' table
        try:
            cursor = self.getcursor()
            sql = "UPDATE part SET Part_No=%s, Part_Name=%s, Price=%s WHERE id=%s"
            cursor.execute(sql, values)
            self.connection.commit()
        finally:
            cursor.close()

    def delete(self, _id):
        # Delete a record from the 'part' table by using its ID
        try:
            cursor = self.getcursor()
            sql = "DELETE FROM part WHERE id = %s"
            values = (_id,)
            cursor.execute(sql, values)
            self.connection.commit()
        finally:
            cursor.close()

    def convert_to_dictionary(self, result):
        # Convert a database result to a dictionary
        col_names = ['id', 'Part_No', 'Part_Name', 'Price']
        return dict(zip(col_names, result)) if result else None

# Instantiate the part_DAO class
partDAO = part_DAO()
