import sqlite3


######################################################


class DB:
    
    @staticmethod
    def connect():      #connection to DataBase
        try:
            conn = sqlite3.connect('DBseeds.db')
            #print("success")
            cursor = conn.cursor()
        except sqlite3.Error as error:
            print(error)
            conn.rollback()
        
        return conn, cursor