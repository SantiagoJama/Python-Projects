from Logic.DAO import DAO


def menu():
    print("************* MAIN MENU ********")
    print("1.- Get classroom")
    print("2.- Save a classroom")
    print("3.- Update a classroom")
    print("4.- Delete a classroom")
    print("5.- Exit")
    user_option = int(input("Enter a option:\t"))

    if user_option < 1 or user_option > 5:
        print("Enter a correct option")
        menu()

    elif user_option == 5:
        print("Good bye")

    else:
        execute_user_option(user_option)


def execute_user_option(user_option):
    Dao = DAO()
    match user_option:
        case 1:

            classroom_data = Dao.get_all_classrooms()
            for cr_id, cr_name, cr_number_student in classroom_data:
                print(f"Classroom id: {cr_id}, classroom name: {cr_name}, classroom number of students: {cr_number_student}")
            menu()
        case 2:
            classroom_name = input("Enter a classroom name:\t")
            classroom_number_of_students = int(input("Enter a number of students:\t "))
            Dao.set_a_classroom(classroom_name, classroom_number_of_students)
            print("Classroom added")
            menu()
        case 3:
            print("---------- All classrooms ---------------")
            classroom_data = Dao.get_all_classrooms()
            for cr_id, cr_name, cr_number_student in classroom_data:
                print(
                    f"Classroom id: {cr_id}, classroom name: {cr_name}, classroom number of students: {cr_number_student}")
            print("-----------------------------------------")
            classroom_id = int(input("Enter a classroom id which you want to update"))
            new_name = input("Enter a new name classroom name for the classroom {}:\t".format(classroom_id))
            new_number_of_students = int(input("Enter the new number of students for the classroom {}:\t ".format(classroom_id)))
            Dao.update_a_classroom(classroom_id, new_name, new_number_of_students)
            print(f"Classroom {classroom_id} updated")
            menu()
        case _:
            print("Not valid option")


menu()
