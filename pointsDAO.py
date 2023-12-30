import mysql.connector
import config as cfg

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

    def create(self, label, penalty_points):
        with self.getcursor() as cursor:
            try:
                sql = "INSERT INTO points (`Drivers cumulative penalty points`, `7182`, `unit_value`, `year_value`) VALUES (%s, %s, %s, %s)"
                values = (label, penalty_points, 'unit_value', 'year_value')
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

    def update(self, values):
        try:
            cursor = self.getcursor()
            sql = "UPDATE points SET `Drivers cumulative penalty points`=%s, `7182`=%s, `unit_value`=%s, `year_value`=%s"
            cursor.execute(sql, values)
            self.connection.commit()
        finally:
            cursor.close()

    def convert_to_dictionary(self, result):
        col_names = ['Drivers cumulative penalty points', '7182', 'unit_value', 'year_value']
        return dict(zip(col_names, result)) if result else None

# Instantiate the points_DAO class
pointsDAO = points_DAO()
