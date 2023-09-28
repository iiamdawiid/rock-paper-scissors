# Rock Paper Scissor Program - User plays against computer and every time user wins
# a random fact is printed with the use of an API
# more practical use of API with hangman game --> (https://github.com/iiamdawiid/hangman-w-api)

import random
import requests

class RockPaperScissor():
    def __init__(self):
        pass

    def game_start(self):
        self.go_again = 0
        self.computer_score = 0
        self.user_score = 0
        print("ROCK PAPER SCISSOR".center(50, '-'))
        start = input("Press ENTER to Start: ")
        while start.isalnum():
            print("\n>>> INVALID INPUT <<<")
            start = input("Press ENTER to Start: ")
        self.game_limit()

    def game_limit(self):
        self.limit = input("Choose # of Rounds: (1),(3),(5): ")
        while self.limit not in {'1', '3', '5'}:
            print("\n>>> INVALID INPUT <<<")
            self.limit = input("Choose # of Rounds: (1),(3),(5): ")
        self.limit = int(self.limit)
        self.running_game()

    def running_game(self):
        while self.go_again < self.limit:
            self.get_user_choice()
        self.game_over() 

    def get_user_choice(self):
        self.user_choice = input("\n(1) Rock\n(2) Paper\n(3) Scissor\nEnter Choice: ")
        while self.user_choice not in {'1', '2', '3'}:
            print("\n>>> INVALID INPUT <<<")
            self.user_choice = input("\n(1) Rock\n(2) Paper\n(3) Scissor\nEnter Choice: ")
        self.user_choice = int(self.user_choice)
        self.computer_choice()

    def computer_choice(self):
        self.comp_choice = random.randint(1,3)
        self.get_outcome()

    def get_random_fact(self):
        url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            random_fact = data['text']
            return random_fact
        else:
            print(f"Status Code: {response.status_code}")

    def get_outcome(self):
        outcomes = {
            (1, 2): "PAPER beats ROCK",
            (2, 1): "PAPER beats ROCK",
            (2, 3): "SCISSOR beats PAPER",
            (3, 2): "SCISSOR beats PAPER",
            (3, 1): "ROCK beats SCISSOR",
            (1, 3): "ROCK beats SCISSOR",
        }

        outcome = 0

        if (self.user_choice, self.comp_choice) in outcomes:
            if self.user_choice != self.comp_choice:
                outcome = 1
                print("\n!! ROUND WON !!")
                print(outcomes[(self.user_choice, self.comp_choice)])
            else:
                print(f"\n!! ROUND TIED !! {self.choice_name(self.user_choice)} ties {self.choice_name(self.comp_choice)}")
        else:
            print("\n!! ROUND LOST !!")

        self.increment_score(outcome)
        self.go_again += 1
        self.print_score()
        if outcome == 1:
            print(self.get_random_fact())

    def increment_score(self, outcome):
        if outcome == 0:
            self.computer_score += 1
        else:
            self.user_score += 1

    def print_score(self):
        print(f"SCORE: ( {self.user_score} : {self.computer_score} )")

    def game_over(self):
        print("")
        print("GAME OVER".center(50, '-'))
        if self.user_score > self.computer_score:
            print("!! YOU WON !!")
        else:
            print("!! YOU LOST !!")
        print(f"SCORE: ( {self.user_score} : {self.computer_score} )")
        self.play_again()

    def play_again(self):
        play_again = input("Play Again? (Y/N): ")
        play_again = play_again.upper()
        while play_again not in {'Y', 'N'}:
            print("\n>>> INVALID INPUT <<<")
            play_again = input("Play Again? (Y/N): ")
            play_again = play_again.upper()
        if play_again == 'Y':
            print("")
            self.game_start()
        else:
            print("\nThank you for playing!")



go = RockPaperScissor()
go.game_start()