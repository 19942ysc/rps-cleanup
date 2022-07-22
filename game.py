



from random import choice

valid_choices = ["rock","paper","scissors"]

#
# USER SELECTION
#

def winner(user_choice, computer_choice):
    if user_choice == "rock" and computer_choice == "rock":
        return("It's a tie!")
    elif user_choice == "rock" and computer_choice == "paper":
        return("The computer wins")
    elif user_choice == "rock" and computer_choice == "scissors":
        return("The user wins")

    elif user_choice == "paper" and computer_choice == "rock":
        #return("The computer wins")
        return("The user wins")
    elif user_choice == "paper" and computer_choice == "paper":
        return("It's a tie!")
    elif user_choice == "paper" and computer_choice == "scissors":
        #return("The user wins")
        return("The computer wins")

    elif user_choice == "scissors" and computer_choice == "rock":
        return("The computer wins")
    elif user_choice == "scissors" and computer_choice == "paper":
        return("The user wins")
    elif user_choice == "scissors" and computer_choice == "scissors":
        return("It's a tie!")


if __name__ == "__main__":


    
    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_choices)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #

    print(winner(u, c))

