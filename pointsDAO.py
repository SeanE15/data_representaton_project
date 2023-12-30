import mysql.connector
import config as cfg
import json

class points_DAO:
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

    def create(self, year, county, label, penalty_points):
        with self.getcursor() as cursor:
            try:
                sql = "INSERT INTO points (`Year`, `County`, `Label`, `PenaltyPoints`) VALUES (%s, %s, %s, %s)"
                penalty_points_str = json.dumps(penalty_points)
                values = (year, county, label, penalty_points_str)
                print("Debug: Values before execution:", values)
                cursor.execute(sql, values)
                self.connection.commit()
                new_id = cursor.lastrowid
            except Exception as e:
                print(f"Error in create: {e}")
                new_id = None
        return new_id

    def getAll(self):
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM points"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [self.convert_to_dictionary(result) for result in results]
        finally:
            cursor.close()

    def convert_to_dictionary(self, result):
        col_names = ['Year', 'County', 'Label', 'PenaltyPoints']
        return dict(zip(col_names, result)) if result else None

# Instantiate the points_DAO class
pointsDAO = points_DAO()
