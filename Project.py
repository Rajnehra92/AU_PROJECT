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

###2
class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        while True:
            user_input = input('''
            1. Press 1 to create PIN
            2. Press 2 to make a withdrawal
            3. Press 3 to check balance
            4. Press 4 to exit
            Enter your choice: ''')
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.withdrawal()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid input. Please try again.")
    def create_pin(self):
        new_pin = input("Enter your new PIN: ")
        new_balance = int(input("Enter your starting balance: "))
        self.pin = new_pin
        self.balance = new_balance
        print("PIN created successfully!")
    def withdrawal(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. New balance is: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect PIN.")
    def check_balance(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print(f"Your current balance is: {self.balance}")
        else:
            print("Incorrect PIN.")
x1=Atm()