# Constants
ROWS = 6  # Number of rows on the Connect 4 board
COLS = 7  # Number of columns on the Connect 4 board
PLAYER1 = 'X'  # Symbol for Player 1
PLAYER2 = 'O'  # Symbol for Player 2

# Initialize board
def create_board():
    """
    Creates a new Connect 4 board.

    Returns:
        list: A 2D list representing an empty Connect 4 board with ROWS rows and COLS columns.
    """
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Print the board
def display_board(board):
    """
    Prints the Connect 4 board to the console in a readable format.

    Args:
        board (list): The current state of the board as a 2D list.
    """
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print('-' * (COLS * 4 + 1))

# Drop a piece into the column
def drop_piece(board, col, piece):
    """
    Drops a player's piece into the specified column if there is space.

    Args:
        board (list): The current state of the board as a 2D list.
        col (int): The column where the player wants to drop their piece.
        piece (str): The symbol representing the player ('X' or 'O').

    Returns:
        int: The row index where the piece lands, or None if the column is full.
    """
    # TODO Implement this function

    pass

# Check if a column is valid for a move
def is_valid_move(board, col):
    """
    Checks if a column has space for another piece.

    Args:
        board (list): The current state of the board as a 2D list.
        col (int): The column number to check.

    Returns:
        bool: True if the column is not full, False otherwise.
    """
    # TODO Implement this function
    pass

# Check for a winning condition
def check_win(board, row, col, piece):
    """
    Checks if placing a piece at the given position creates a win.

    Args:
        board (list): The current state of the board as a 2D list.
        row (int): The row index where the piece was placed.
        col (int): The column index where the piece was placed.
        piece (str): The symbol representing the player ('X' or 'O').

    Returns:
        bool: True if there are four consecutive pieces in any direction, False otherwise.
    """
    # TODO Implement this function
    pass



# Switch player turn
def switch_player(piece):
    """
    Switches the active player.

    Args:
        piece (str): The current player's symbol ('X' or 'O').

    Returns:
        str: The symbol of the next player ('O' if current player is 'X', otherwise 'X').
    """
    # TODO: Implement this function
    pass

# Main game loop
def play_connect4():
    """
    Main function to control the game loop. Manages player turns, checks for valid moves,
    updates the board, and checks for a winning condition after each move.
    """
    board = create_board()
    game_over = False
    turn = PLAYER1

    display_board(board)

    while not game_over:
        # Ask for user input
        try:
            col = int(input(f"Player {turn}, choose a column (1-{COLS}): "))
            # Check if the column choice is valid
            if not is_valid_move(board, col):
                print("Invalid move. Try again.")
                continue
            
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        # Drop the piece
        # TODO: Implement the drop_piece function to allow this part to work.
        
        # Check for a win
        # TODO: Implement the check_win function to check for a winning condition.
        
        # Switch players
        turn = switch_player(turn)

# Run the game
play_connect4()
