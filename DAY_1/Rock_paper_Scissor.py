import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
         _______)
        _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
      __________)
      (_____)
---.__(___)
'''
game = [rock, paper, scissors]

while True:
    user = int(input("\nEnter 0 for Rock, 1 for Paper, 2 for Scissors : "))
    if user >= 0 and user <= 2:
        print("\nYou chose:")
        print(game[user])

        comp = random.randint(0, 2)

        print("Computer chose:")
        print(game[comp])

        if user == comp:
            print("Draw")
        elif user == 0 and comp == 2:
            print("You Win")
        elif user == 2 and comp == 0:
            print("You Lose")
        elif user > comp:
            print("You Win")
        else:
            print("You Lose")
            
    else:
        print("Invalid Input")

    ch = input("\nPlay again? (y/n) : ")

    if ch.lower() != "y":
        break