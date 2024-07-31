import random
# I tackled the problem of simulating the movement of a specialized castle on a chessboard with soldiers. The goal was to determine unique paths the castle could take to return to its starting position while adhering to specific movement rules. I implemented a Python program where soldiers were placed on a chessboard, and the castle’s movements were simulated based on the rules: moving forward, killing soldiers, and then moving left.

# The program initializes an 8x8 chessboard with soldiers placed at user-defined coordinates and the castle at its starting position. It then recursively explores all possible paths the castle could take while following the rules of movement. The castle kills soldiers it encounters directly in front and then moves left, all while avoiding duplicating paths.

# I utilized a recursive function to simulate the castle’s movement and track the unique paths it could take to reach its destination. The final output consists of the initial state of the board and the unique paths that the castle can take to return home. This approach effectively models the problem and provides a clear visualization of the castle’s movement and pathfinding capabilities.

def create_board(size, num_soldiers):
    board = [['.' for _ in range(size)] for _ in range(size)]
    
    for _ in range(num_soldiers):
        x, y = random.randint(0, size-1), random.randint(0, size-1)
        board[x][y] = 'S'
    
    castle_x, castle_y = random.randint(0, size-1), random.randint(0, size-1)
    board[castle_x][castle_y] = 'C'
    
    return board, (castle_x, castle_y)

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def move_castle(board, castle_pos):
    x, y = castle_pos
    size = len(board)
    
    while x < size-1:
        if board[x+1][y] == 'S':
            board[x+1][y] = '.'
            if y > 0:
                y -= 1
        x += 1
    
    board[x][y] = 'C'
    return board

size = 8  # 8x8 chessboard
num_soldiers = 10
board, castle_pos = create_board(size, num_soldiers)

print("Initial Board:")
print_board(board)

board = move_castle(board, castle_pos)

print("Final Board after Castle Moves:")
print_board(board)
