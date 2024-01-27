logo = """
$$$$$$$$\$$$$$$\ $$$$$$\        $$$$$$$$\ $$$$$$\  $$$$$$\        $$$$$$$$\ $$$$$$\ $$$$$$$$\ 
\__$$  __\_$$  _$$  __$$\       \__$$  __$$  __$$\$$  __$$\       \__$$  __$$  __$$\$$  _____|
   $$ |    $$ | $$ /  \__|         $$ |  $$ /  $$ $$ /  \__|         $$ |  $$ /  $$ $$ |      
   $$ |    $$ | $$ |               $$ |  $$$$$$$$ $$ |               $$ |  $$ |  $$ $$$$$\    
   $$ |    $$ | $$ |               $$ |  $$  __$$ $$ |               $$ |  $$ |  $$ $$  __|   
   $$ |    $$ | $$ |  $$\          $$ |  $$ |  $$ $$ |  $$\          $$ |  $$ |  $$ $$ |      
   $$ |  $$$$$$\\$$$$$$  |         $$ |  $$ |  $$ \$$$$$$  |         $$ |   $$$$$$  $$$$$$$$\ 
   \__|  \______|\______/          \__|  \__|  \__|\______/          \__|   \______/\________|
   """

start_boardgame = """
   7  |   8  |   9
---------------------
   4  |   5  |   6
---------------------
   1  |   2  |   3
"""
start_positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

players = {
    "Player X": [],
    "Player O": []
}

winner_lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                [1, 4, 7], [2, 5, 8], [3, 6, 9],
                [1, 5, 9], [3, 5, 7]]


def any_winner(player):
    for winner_line in winner_lines:
        winner = all(item in players[player] for item in winner_line)
        if winner:
            return True


def play():
    global boardgame
    global players
    global free_positions

    for player in players:
        print(boardgame)
        print(player)
        player_movement = input("Choose your movement: ")
        players[player].append(int(player_movement))
        free_positions.remove(int(player_movement))

        if player == "Player X":
            boardgame = boardgame.replace(player_movement, "X")

        elif player == "Player O":
            boardgame = boardgame.replace(player_movement, "O")

        if any_winner(player):
            print(f"    {player}\nYOU´RE THE WINNER!")
            print(boardgame)
            break

        if len(free_positions) == 0:
            print("IT´S A DRAW!")
            print(boardgame)
            break

    if not any_winner(player) and len(free_positions) > 0:
        print("repeat")
        play()


print(logo)
running_game = input("Do you want to play TIC TAC TOE? Type 'y' or 'n': ")

while running_game == "y":
    print("Just click on the number where you want to move!")
    players['Player X'].clear()
    players['Player O'].clear()
    boardgame = start_boardgame
    free_positions = start_positions[:]
    play()
    running_game = input("Play again? Type 'y' or 'n': ")
    if running_game == "n":
        print("Good Bye")
