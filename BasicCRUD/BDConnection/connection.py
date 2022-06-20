import mysql.connector as mc
from mysql.connector import Error


class Connection:

    def __init__(self):
        try:
            self.__connection = mc.connect(
                host="",
                port=0000,
                user="",
                password="",
                db=""
            )
        except Error as err:
            print("Error -> {}".format(err))

    def get_connection(self):
        if self.__connection.is_connected():
            try:
                return self.__connection
            except Error as err:
                print("Error -> {}".format(err))

