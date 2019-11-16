from random import randint                                      # import only randint function from "random" package
print("__---Rock Paper Scissors---__")
player_score = 0                                                # initialize player and computer scores to zero
computer_score = 0
points = int(input("Set the target point for the match:"))

while player_score != points and computer_score != points:      # loops until either player or computer reaches 5 points

    player1 = input("Player enter your choice:\n").lower()      # .lower() converts string to lower case
    rand_no = randint(0, 2)                                     # randomly chooses a number between 0 and 2
    if rand_no == 0:
        computer = "rock"
        print("Computer chooses Rock")                          # 0-rock; 1-paper; 2-scissors
    elif rand_no == 1:
        computer = "paper"
        print("Computer chooses Paper")
    else:
        computer = "scissors"
        print("Computer chooses Scissors")

    if player1 == computer:
        print("It's a Tie! ")
    elif player1 == "rock":
        if computer == "paper":
            print("Computer wins the round! ")
            computer_score += 1
        else:
            print("Player wins the round! ")
            player_score += 1
    elif player1 == "paper":
        if computer == "scissors":
            print("Computer wins the round! ")
            computer_score += 1
        else:
            print("Player wins the round! ")
            player_score += 1
    elif player1 == "scissors":
        if computer == "rock":
            print("Computer wins the round! ")
            computer_score += 1
        else:
            print("Player wins the round! ")
            player_score += 1
    else:
        print("Give proper value ")

    print(f"Player {player_score} points")
    print(f"Computer {computer_score} points")

if player_score == points:
    print("Player Wins the match!")
else:
    print("Computer Wins the match!")

