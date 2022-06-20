from BasicCRUD.BDConnection.connection import Connection
from mysql.connector import DataError


class DAO:

    def __init__(self):
        self.__connection = Connection().get_connection()
        self.__cursor = self.__connection.cursor()

    def get_all_classrooms(self):
        try:
            self.__cursor.execute(
                "Select *from classroom;"
            )
            return self.__cursor.fetchall()
        except DataError as err:  # It is not a correct error, for now. It is for testing purpose
            print("Error -> {}".format(err))

    def set_a_classroom(self, classroom_name, classroom_number_of_students):
        try:
            self.__cursor.execute(
                "INSERT INTO classroom values(cr_id,'{}','{}')".format(classroom_name, classroom_number_of_students))
            self.__connection.commit()
        except DataError as err:  # It is not a correct error, for now. It is for testing purpose
            print("ERROR -> {}".format(err))

    def update_a_classroom(self, classroom_id, new_name, new_number_of_students):
        try:
            self.__cursor.execute(
                "UPDATE classroom SET cr_name = '{}', cr_number_student = '{}' WHERE cr_id = '{}';".format(new_name,
                                                                                                           new_number_of_students,
                                                                                                           classroom_id))
            self.__connection.commit()
        except DataError as err:  # It is not a correct error, for now. It is for testing purpose
            print("ERROR -> {}".format(err))

    def delete_a_classroom(self, classroom_id):
        try:
            self.__cursor.execute("DELETE FROM classroom WHERE cr_id = '{}'".format(classroom_id))
            self.__connection.commit()
        except DataError as err:
            print("ERROR ---> {}".format(err))

    def close_connection(self):
        self.__connection.close()
