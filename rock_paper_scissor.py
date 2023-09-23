import random

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

    def get_outcome(self):
        outcome = 0
        print("")
        if self.user_choice == 1 and self.comp_choice == 2:
            print("!! ROUND LOST !!")
            print("PAPER beats ROCK")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        elif self.user_choice == 2 and self.comp_choice == 1:
            outcome = 1
            print("!! ROUND WON !!")
            print("PAPER beats ROCK")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        elif self.user_choice == 2 and self.comp_choice == 3:
            print("!! ROUND LOST !!")
            print("SCISSOR beats PAPER")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        elif self.user_choice == 3 and self.comp_choice == 2:
            outcome = 1
            print("!! ROUND WON !!")
            print("SCISSOR beats PAPER")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        elif self.user_choice == 3 and self.comp_choice == 1:
            print("!! ROUND LOST !!")
            print("ROCK beats SCISSOR")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        elif self.user_choice == 1 and self.comp_choice == 3:
            outcome = 1
            print("!! ROUND WON !!")
            print("ROCK beats SCISSOR")
            self.increment_score(outcome)
            self.go_again += 1
            self.print_score()
        else:
            print("!! ROUND TIED !!")
        

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
            return



go = RockPaperScissor()
go.game_start()