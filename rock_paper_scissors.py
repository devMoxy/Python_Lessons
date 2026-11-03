import random
#1 - Rock, 2 - Paper, 3 - Scissors

def win(player, computerMove):
    print(f"\nYou choose {player.upper()} and computer choose {computerMove.upper()} \nYou WIN!!!")

def lose(player, computerMove):
    print(f"\nYou choose {player.upper()} and computer choose {computerMove.upper()} \nYou LOSE!!!")

def draw(player, computerMove):
    print(f"\nYou choose {player.upper()} and computer choose {computerMove.upper()} \nIt's a draw!!!")

while True:
    print("\nWelcome to Rock Paper Scissors Game")
    player = input("Choose between Rock, Paper and Scissors: ")

    if player.lower() != "rock" or player.lower() != "paper" or player.lower() != "scissors":
        print("Enter either Rock, Paper and Scissors to play\nTry again!!!")

    computer = random.randint(1,3)
    if computer == 1:
        computerMove = "Rock"
    elif computer == 2:
        computerMove = "Paper"
    else:
        computerMove = "Scissors"

    if computerMove == "Rock" and player.lower() == "rock":
        draw(player, computerMove)
    elif computerMove == "Rock" and player.lower() == "paper":
        win(player, computerMove)
    elif computerMove == "Rock" and player.lower() == "scissors":
        win(player, computerMove)

    elif computerMove == "Paper" and player.lower() == "paper":
        draw(player, computerMove)
    elif computerMove == "Paper" and player.lower() == "scissors":
        win(player, computerMove)
    elif computerMove == "Paper" and player.lower() == "rock":
        lose(player, computerMove)

    elif computerMove == "Scissors" and player.lower() == "scissors":
        draw(player, computerMove)
    elif computerMove == "Scissors" and player.lower() == "rock":
        win(player, computerMove)
    elif computerMove == "Scissors" and player.lower() == "paper":
        lose(player, computerMove)