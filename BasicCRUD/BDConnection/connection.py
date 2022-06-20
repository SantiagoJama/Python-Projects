import mysql.connector as mc
from mysql.connector import Error


class Connection:

    def __init__(self):
        try:
            self.connection = mc.connect(
                host="",
                port=000,
                user="",
                password="",
                db=""
            )
        except Error as err:
            print("Error -> {}".format(err))

    def get_connection(self):
        if self.connection.is_connected():
            try:
                return self.connection
            except Error as err:
                print("Error -> {}".format(err))
