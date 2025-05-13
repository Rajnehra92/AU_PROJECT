# flashcard code....
import random

class FlashCard:
    def __init__(self):  # FIX: Corrected __init__ method name
        self.fruits = {
            "Banana": "yellow",
            "Strawberries": "pink",
            "Watermelon": "green",
            "Apple": "red",
            "Blueberry": "blue"
        }

    def play(self):
        print("Welcome to the fruit quiz!")
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            answer = input(f"What is the color of {fruit}? ").strip().lower()
            if answer == color:
                print("Correct answer!")
            else:
                print(f"Wrong answer. The correct color is {color}.")

            play_again = input("Play again? (yes/no): ").strip().lower()
            if play_again != "yes":
                break

# Create an instance and start the game
flash_card = FlashCard()
flash_card.play()