import mysql.connector
import main
class DBHandler:
    def __init__(self):
        DBHandler.HOST = main.HOST
        DBHandler.USER = main.USER
        DBHandler.DBNAME = main.DATABASE
        DBHandler.PASSWORD = main.PASS
    HOST = main.HOST
    USER = main.USER
    DBNAME = main.DATABASE
    PASSWORD = main.PASS
    @staticmethod
    def get_mydb():
        if DBHandler.DBNAME == '':
            main.init()
        db = DBHandler()
        mydb = db.connect()
        return mydb

    def connect(self):
        mydb = mysql.connector.connect(
            host=DBHandler.HOST,
            user=DBHandler.USER,
            passwd=DBHandler.PASSWORD,
            database = DBHandler.DBNAME
        )
        return mydb