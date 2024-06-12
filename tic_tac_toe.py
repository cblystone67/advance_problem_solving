

board = [' ' for _ in range(9)]

def display_board(board):
  for i in range(3):
    print(' | '.join(board[i*3:(i+1)*3]))

def get_player_move(player):
  while True:
    try:
      move = int(input(f"Player {player}, enter your move (1-9): "))
      if 0 < move <= 9 and board[move - 1] == ' ':
        return move - 1
      else:
        print("Invalid move. Try again.")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 9.")
def place_move(board, move, player):
  board[move] = player
  
def check_winner(board, player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for row in win_conditions:
    if all(board[i] == player for i in row):
      return True
  return False




def main():
  current_player = 'X'
  game_over = False
  while not game_over:
    display_board(board)
    move = get_player_move(current_player)
    place_move(board, move, current_player)

    if check_winner(board, current_player):
      display_board(board)
      print(f"Player {current_player} wins!")
      game_over = True
    else:
      # Check for tie (all spaces filled)
      if all(x != ' ' for x in board):
        print("It's a tie!")
        game_over = True

    # Switch player for next turn
    current_player = 'O' if current_player == 'X' else 'X'
  
if __name__ == "__main__":
  main()
  
  
