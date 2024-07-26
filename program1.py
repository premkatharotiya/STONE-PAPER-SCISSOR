""" STONE PAPER PANCIL SCISSORS GAME
    STONE 1
    PAPER 2
    PANCIL 3
    SCICCOR 4
"""
import random

print("\nLet's Play Stone, Paper, Pencil, & Scissor")
print("1. Stone\n2. Paper\n3. Pencil\n4. Scissor\n")

dict = {"Stone": 1, "Paper": 2, "Pencil": 3, "Scissor": 4}
reverse_dict = {1: "Stone", 2: "Paper", 3: "Pencil", 4: "Scissor"}

your_points = 0
computer_points = 0

for i in range(1, 11):
    print(f"Round: {i}")

    user_choice = input("Enter your choice (Stone, Paper, Pencil, Scissor): ")
    print("\n")
    if user_choice not in dict:
        print("Invalid choice.Plz enter first capital later.\n")
        continue
    
    user_choice_num = dict[user_choice]
    print(f"Your choice: {user_choice}")

    computer_choice_num = random.choice([1, 2, 3, 4])
    computer_choice = reverse_dict[computer_choice_num]
    print(f"Computer choice: {computer_choice}\n")

    if user_choice_num == computer_choice_num:
        print("Oops, it's a draw.\n")
    elif (user_choice_num == 1 & (computer_choice_num == 3 or computer_choice_num == 4)):
          print("Excellent, you win this round!\n")
          your_points += 1
         
    elif (user_choice_num == 2 & computer_choice_num == 1):
         print("Excellent, you win this round!\n")
         your_points +=1
        
    elif(user_choice_num == 3 & computer_choice_num == 2):
         print("Excellent, you win this round!\n")
         your_points +=1

    elif(user_choice_num == 4 & (computer_choice_num == 2 or computer_choice_num == 3)):
        print("Excellent, you win this round!\n")
        your_points += 1
    else:
        print("Computer wins this round.\n")
        computer_points += 1

    
    print(f"Your points: {your_points}")
    print(f"Computer points: {computer_points}\n")


if your_points > computer_points:
    print("\nWonderful performance, you win the game!")
elif your_points == computer_points:
    print("Oops, it's a draw.")
else:
    print("You lose this game. Better luck next time!")
