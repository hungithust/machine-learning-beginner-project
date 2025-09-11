
def print_board(board):
    for i, row in enumerate(board):
        row_str=' '
        for j, cell in enumerate(row):
            row_str +=cell
            if j !=len(row) - 1:
                row_str += ' | '
        
        
        print(row_str)
        if i != len(board) - 1:
            print ('---------')
        

def get_move(turn, board):
    while True:
        row = int(input("Row: "))
        col = int(input("Col: "))
        if row >0 and row <= len(board) and col >0 and col <= len(board):
            if board[row-1][col-1] == ' ':
                board[row-1][col-1] = turn
                print("done")
                break
            else :
                print("Cell already occupied. Try again.")
                continue
        
        else:
            print("Invalid move. Try again.")
            continue


def check_winner(board):
    #row
    for row in board:
        if row[0] == row[1] == row[2] !=' ':
            if row[0] == 'X':
                print("X player wins!")
                

board =[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]



turn_count = 0
win = False
turn = input("Choose who goes first? (X/O): ").upper()

if turn != 'X' and turn != 'O':
    print("Invalid choice. Defaulting to X.")
    turn = 'X'

while win == False:
    
    if turn_count != 9:
        print(f"It is {turn} player turn. Please select you move.")
        get_move(turn, board)
        print_board(board)
        turn_count +=1
        win = check_winner(board)
    
print("Test")