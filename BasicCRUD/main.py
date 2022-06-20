from Dao.DAO import DAO


def menu():
    print("************* MAIN MENU ********")
    print("1.- Get all classrooms")
    print("2.- Save a classroom")
    print("3.- Update a classroom")
    print("4.- Delete a classroom")
    print("5.- Exit")

    try:
        user_option = int(input("Enter a option:\t"))
        if user_option < 1 or user_option > 5:
            print("Enter a correct option")
            menu()
        else:
            execute_user_option(user_option)

    except ValueError as ve:
        print("=========== ERROR----> You enter should be a number, not a string your enter: {}=======".format(ve))
        menu()




def print_result(data):
    Table = """\
    +---------------------------------------------------------+
    | Classroom Id    Classroom Name       Number of students |
    |---------------------------------------------------------|
    {}
    +---------------------------------------------------------+\
    """
    Table = (Table.format('\n'.join("|{:>6} {:>21} {:>17}           |".format(cr_id, cr_name, cr_number_student)
                                    for cr_id, cr_name, cr_number_student in data)))
    print(Table)

def execute_user_option(user_option):
    Dao = DAO()
    match user_option:
        case 1:
            classroom_data = Dao.get_all_classrooms()
            print_result(classroom_data)
            menu()
        case 2:
            classroom_name = input("Enter a classroom name:\t")
            classroom_number_of_students = int(input("Enter a number of students:\t "))
            Dao.set_a_classroom(classroom_name, classroom_number_of_students)
            print("=========== Classroom added ===========")
            menu()
        case 3:
            print("---------- All classrooms ---------------")
            classroom_data = Dao.get_all_classrooms()
            print_result(classroom_data)
            print("-----------------------------------------")
            classroom_id = int(input("Enter a classroom id which you want to update"))
            new_name = input("Enter a new name classroom name for the classroom {}:\t".format(classroom_id))
            new_number_of_students = int(input("Enter the new number of students for the classroom {}:\t ".format(classroom_id)))
            Dao.update_a_classroom(classroom_id, new_name, new_number_of_students)
            print(f"======= Classroom {classroom_id} updated ========")
            menu()

        case 4:
            print("---------- All classrooms ---------------")
            classroom_data = Dao.get_all_classrooms()
            print_result(classroom_data)
            print("-----------------------------------------")
            class_room_to_delete = int(input("Enter a classroom id to delete:\t"))
            print("Are you sure you want to delete a classroom with id {}?".format(class_room_to_delete))
            confirmation = int(input("Yes = 1\nNo = 0 \n Your answer:\t"))
            if confirmation == 1:
                Dao.delete_a_classroom(class_room_to_delete)
                print("========== Classroom deleted ===========")
                menu()
            else:
                print("=========== Operation cancelled ===========")
                menu()
        case 5:
            print("========== Good bye ===========")
            Dao.close_connection()
        case _:
            print("========== Not valid option ========")

menu()
