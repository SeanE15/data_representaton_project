import mysql.connector
import config as cfg

class part_DAO:
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None
        self.cursor = None

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close_all(self):
        if self.connection:
            self.connection.close()
        if self.cursor:
            self.cursor.close()

    def create(self, values):
        with self.getcursor() as cursor:
            sql = "INSERT INTO part (id, Part_No, Part_Name, Price) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, values)
            self.connection.commit()
            new_id = cursor.lastrowid
        return new_id

    def get_all(self):
        with self.getcursor() as cursor:
            sql = "SELECT * FROM part"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [self.convert_to_dictionary(result) for result in results]

    def find_by_id(self, _id):
        with self.getcursor() as cursor:
            sql = "SELECT * FROM part WHERE id = %s"
            values = (_id,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return self.convert_to_dictionary(result) if result else None

    def update(self, values):
        with self.getcursor() as cursor:
            sql = "UPDATE part SET Part_No=%s, Part_Name=%s, Price=%s WHERE id=%s"
            cursor.execute(sql, values)
            self.connection.commit()

    def delete(self, _id):
        with self.getcursor() as cursor:
            sql = "DELETE FROM part WHERE id = %s"
            values = (_id,)
            cursor.execute(sql, values)
            self.connection.commit()

    def convert_to_dictionary(self, result):
        col_names = ['id', 'Part_No', 'Part_Name', 'Price']
        return dict(zip(col_names, result)) if result else None

# Instantiate the part_DAO class
partDAO = part_DAO()
