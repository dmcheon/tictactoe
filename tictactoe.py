def checkCells(c1: int, c2: int, c3: int, c4: int) -> bool:
    """
    Check if four cells have the same non-zero value.

    param c1 to c4: First to Fourth cell values
    return: True if all four cells are the same and not zero, else False
    """
    return c1 == c2 == c3 == c4 != 0
    
def checkVertical(board: list) -> int:
    """
    Check all vertical columns for four matching non-zero values.

    return: The value of the winner (1 or 2) if found, otherwise 0
    """
    # Alternativly, 
    # return checkHorizontal(list(zip(*board)))

    size = len(board)
    for i in range(size):
        if checkCells(board[0][i],board[1][i],board[2][i],board[3][i]):
            return board[0][i]
    return 0

def checkHorizontal(board: list) -> int:
    size = len(board)
    for i in range(size):
        if checkCells(board[i][0],board[i][1],board[i][2],board[i][3]):
            return board[i][0]
    return 0

def checkDiagonal(board: list) -> int:
    if checkCells(board[0][0],board[1][1],board[2][2],board[3][3]):
        return board[0][0]
    if checkCells(board[0][3], board[1][2], board[2][1], board[3][0]):
        return board[0][3]
    return 0

def check4Corners(board: list) -> int:
    if checkCells(board[0][0], board[0][3], board[3][0], board[3][3]):
        return board[0][0]
    return 0
    
def check2by2box(board: list) -> int:
    size = len(board) - 1
    for y in range(size):
        for x in range(size):
            if checkCells(board[y][x], board[y][x + 1], board[y + 1][x], board[y + 1][x + 1]):
                return board[y][x]
    return 0
        

def checkWinner(board: list) -> int:
    """
    Check the board for a winner by using various check functions.

    return: The value of the winner if found, otherwise 0
    """
    checkFuctions = [
        checkVertical, 
        checkHorizontal, 
        checkDiagonal, 
        check4Corners, 
        check2by2box
    ]
    
    for func in checkFuctions:
        result = func(board)
        if result != 0:
            return result
    return 0
    
    
def anyMovesLeft(board: list) -> bool:
    size = len(board)
    for y in range(size):
        for x in range(size):
            if board[y][x] == 0:
                return True
    return False
    
    
def isGameOver(board: list, winner: int) -> bool:
    if winner > 0:
        return True
    else:
        return not anyMovesLeft(board)
    

def main():
    # board: 2D list representing the 4x4 tic-tac-toe board
    # 0 means empty cell, 1 means the first player's move
    # and 2 means the second player's move
    
        
    # get user input
    board = [list(map(int, input().split())) for _ in range(4)]
    
    # sanity check
    for row in board:
        if len(row) != 4:
            raise ValueError("Each row should have four inputs.")
        
    winner = checkWinner(board)

    if isGameOver(board, winner):
        if winner == 0:
            print("Tie")
        elif winner == 1:
            print("First player wins!")
        elif winner == 2:
            print("Second player wins!")
        else:
            raise ValueError()
    else:
        print("Continue")
     
        
if __name__ == "__main__":
    main()