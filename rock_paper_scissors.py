import random
#1 - Rock, 2 - Paper, 3 - Scissors

def win(computerMove, player):
    print(f"\nYou choose {player} and computer choose {computer} \nYou WIN!!!")

def lose(computerMove, player):
    print(f"\nYou choose {player} and computer choose {computer} \nYou LOSE!!!")

def draw(computerMove, player):
    print(f"\nYou choose {player} and computer choose {computer} \nIt's a draw!!!")

while True:
    print("\nWelcome to Rock Paper Scissors Game")
    player = input("Choose between Rock, Paper and scisors: ")
    computer = random.randint(1,3)
    if computer == 1:
        computerMove = "Rock"
    elif computer == 2:
        computerMove = "Paper"
    else:
        computerMove = "Scissors"

    print(computerMove)

    if computerMove == "Rock" and player.lower() == "rock":
        draw(player, computerMove)