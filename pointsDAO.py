import mysql.connector
import config as cfg

class points_DAO:
    def __init__(self):
        # Initialize points_DAO with database connection details from config
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
        # Create a new record in the 'points' table
        with self.getcursor() as cursor:
            try:
                # Fix the SQL query to properly handle column names with spaces
                sql = 'INSERT INTO points ("Male", "Female", "No_gender_recorded", "All_genders") VALUES (%s, %s, %s, %s)'
                print("Debug: Values before execution:", values)

                # Convert the values to integers before insertion
                values = tuple(int(value) for value in values)

                cursor.execute(sql, values)
                self.connection.commit()
                new_id = cursor.lastrowid
            except Exception as e:
                print(f"Error in create: {e}")
                new_id = None
        return new_id

    def getAll(self):
        # Retrieve all records from the 'points' table
        cursor = self.getcursor()
        sql = "SELECT * FROM points"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


    def convert_to_dictionary(self, result):
        # Convert a database result to a dictionary
        col_names = ["Male", "Female", "No_gender_recorded", "All_genders"]
        return dict(zip(col_names, result)) if result else None

# Instantiate the points_DAO class
pointsDAO = points_DAO()
