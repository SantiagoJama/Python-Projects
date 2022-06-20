from BasicCRUD.BDConnection.connection import Connection


class DAO:

    def __init__(self):
        self.connection = Connection()
        #self.cursor = self.connection.get_connection().cursor()

    def get_all_classrooms(self):
        try:
            cursor = self.connection.get_connection().cursor()
            cursor.execute(
                "Select *from classroom;"
            )
            return cursor.fetchall()
        except NameError as err:  # It is not a correct error, for now. It is for testing purpose
            print("Error -> {}".format(err))

    def set_a_classroom(self, classroom_name, classroom_number_of_students):
        try:
            cursor = self.connection.get_connection().cursor()
            cursor.execute("INSERT INTO classroom values(cr_id,'{}','{}')".format(classroom_name, classroom_number_of_students))
            self.connection.get_connection().commit()
        except NameError as err: # It is not a correct error, for now. It is for testing purpose
            print("ERROR -> {}".format(err))

    def update_a_classroom(self, classroom_id, new_name, new_number_of_students):
        try:
            cursor = self.connection.get_connection().cursor()
            cursor.execute("UPDATE classroom SET cr_name = '{}', cr_number_student = '{}' WHERE cr_id = '{}';".format(new_name, new_number_of_students, classroom_id))
            self.connection.get_connection().commit()
        except NameError as err: # It is not a correct error, for now. It is for testing purpose
            print("ERROR -> {}".format(err))
