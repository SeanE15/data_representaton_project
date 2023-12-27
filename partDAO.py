import mysql.connector
import config as cfg

class part_DAO:
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return self.connection.cursor()

    def close_all(self):
        if self.connection:
            self.connection.close()

    def create(self, values):
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
        return new_id


    def getAll(self):
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM part"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [self.convert_to_dictionary(result) for result in results]
        finally:
            cursor.close()

    def find_by_id(self, _id):
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
        try:
            cursor = self.getcursor()
            sql = "UPDATE part SET Part_No=%s, Part_Name=%s, Price=%s WHERE id=%s"
            cursor.execute(sql, values)
            self.connection.commit()
        finally:
            cursor.close()

    def delete(self, _id):
        try:
            cursor = self.getcursor()
            sql = "DELETE FROM part WHERE id = %s"
            values = (_id,)
            cursor.execute(sql, values)
            self.connection.commit()
        finally:
            cursor.close()

    def convert_to_dictionary(self, result):
        col_names = ['id', 'Part_No', 'Part_Name', 'Price']
        return dict(zip(col_names, result)) if result else None

# Instantiate the part_DAO class
partDAO = part_DAO()
