import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choise = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
print(game_images[user_choise])
computer_choise = random.randint(0, 2)
print("Computer chose: ")
print(game_images[computer_choise])
if user_choise >= 3 or user_choise < 0:
  print("Enter correct digit")
elif user_choise == 0 and computer_choise == 2:
  print(" You win!")
elif user_choise == 2 and computer_choise == 0:
  print(" You lose!")
elif user_choise > computer_choise:
  print(" You win!")
elif user_choise < computer_choise:
  print(" You lose!")
elif user_choise == computer_choise:
  print("It is a draw!")