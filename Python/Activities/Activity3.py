Player1 =input("What is Player 1's name? ")
Player2 = input("What is Player 2's name? ")

#user choice for paper or scissors?
Player1_choice = input(Player1+ ", do you want rock ,paper or scissors?").lower()
Player2_choice = input(Player2+ ", do you wantrock , paper or scissors?").lower()

if Player1_choice == Player2_choice :
    print("Its a tie")
elif Player1_choice == "rock":
    if Player2_choice == "scissors":
        print("rock wins!!")
    else:
        print("Paper wins!")
elif Player1_choice == 'scissors':
    if Player2_choice == 'paper':
        print("Scissors win!")
    else:
        print("Rock wins!")
elif Player1_choice == 'paper':
    if Player2_choice == 'rock':
        print("Paper wins!")
    else:
        print("Scissors win!")
else:
    print("Invalid input! Please select correct option then try again.")
