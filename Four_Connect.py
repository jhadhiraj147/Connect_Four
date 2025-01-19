class Connect_four:

    def make_board(size):
        # input is a tuple
        board = []
        for i in range(size[0]):
            board.append([])
            for j in range(size[1]):
                board[-1].append(0)
        return board
    

    def is_board_full(board):
        for row in board:
            if 0 in row:
                return False
        return True


    def print_board(board):
        for row in board:
            for element in row:
                print(element, end = " ")
            print()
        return



    def make_move(column, letter, board):
        for row_number in range(len(board) - 1, -1, -1):
            if board[row_number][column] == 0:
                board[row_number][column] = letter
                return



    def win_checker(board):
        total_rows = len(board)
        total_columns = len(board[0]) 

        for i in range(total_rows):
            for j in range(total_columns):
                # Check horizontal
                if j <= total_columns - 4:  # Ensure there are at least 4 columns remaining
                    if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3]:
                        return board[i][j]
                
                # Check vertical
                if i <= total_rows - 4:  # Ensure there are at least 4 rows remaining
                    if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j]:
                        return board[i][j]
                
                # Check diagonal (down-right)
                if i <= total_rows - 4 and j <= total_columns - 4:  # Ensure enough space for a diagonal
                    if board[i][j] != 0 and board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3]:
                        return board[i][j]
                
                # Check diagonal (up-right)
                if i >= 3 and j <= total_columns - 4:  # Ensure enough space for an upward diagonal
                    if board[i][j] != 0 and board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3]:
                        return board[i][j]

    

        
game = Connect_four
i = int(input("Enter the number of rows: "))
j = int(input("Enter the number of columns: "))
board = game.make_board((i, j))
print("Game Initialized")
print("Board resetted to default 0")
game.print_board(board)


while True:
    if not game.is_board_full(board):
        print("Player A turn")
        column = int(input("Enter the column you are choosing: "))
        game.make_move(column, "A", board)
        game.print_board(board)
        if game.win_checker(board) in ("A", "B"):
            print("The Winner is: ", game.win_checker(board))
            break

    else:
        print("Game Draw")
        game.print_board
        break

    if not game.is_board_full(board):
        print("Player B turn")
        column = int(input("Enter the column you are choosing: "))
        game.make_move(column, "B", board)
        game.print_board(board)
        if game.win_checker(board) in ("A", "B"):
            print("The Winner is: ", game.win_checker(board))
            break

    else:
        print("Game Draw")
        game.print_board
        break


    
        
    






