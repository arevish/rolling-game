import random

def main():
    player1 = 0
    player2 = 0
    player1wins = 0
    player2wins = 0
    rounds = 1

    while rounds !=4:
        print("Round" + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player1 Roll:" + str(player1))
        print("Player2 Roll:" + str(player2))

        if player1 == player2:
            print("DRAW\n")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Player1 WINS!\n")
        else:
            player2wins = player2wins + 1
            print("Player2 WINS!\n")

        rounds = rounds + 1
    
    if player1wins == player2wins:
        print("DRAW")
    elif player1wins > player2wins:
        print("Player 1 WINS! Rounds won: " + str(player1wins))
    else:
        print("Player 2 WINS! Rounds won: " + str(player2wins))

def dice_roll ():
    diceroll = random.randint(1, 6)
    return diceroll

main()