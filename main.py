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
      (____)
---.__(___)
'''

#Write your code below this line
print("Welcome to the Rock, Paper, and Scissors Game")
user_choice = int(input("What number do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")

#2 beats 1, 1 beats 0, 0 beats 2 
if user_choice == 0 and computer_choice == 2:
  print("You win") 
elif computer_choice > user_choice: 
  print("You lose")



