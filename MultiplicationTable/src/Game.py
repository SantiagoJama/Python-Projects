
class Game:
    type_game_description = ""

    def __init__(self, amount_of_life, points_to_win):
        self.amount_of_life = amount_of_life
        self.points_to_win = points_to_win

    def get_user_option(self):
        while True:
            user_response = input("Choose a option:\n")

    def show_description_game(self):
        print(self.type_game_description)

    def show_win_message(self):
        print("You won!")

    def show_defeat_message(self):
        print("You lose!")


