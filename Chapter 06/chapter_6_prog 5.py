queenscnt = 0

def IsSafe (board, row, col) :
   # Check if there is a queen 'Q' on the left of col in same row.
   for c in range(col) :
       if (board[row][c] == 'Q') :
           return False

   # Check if there is a queen 'Q' on the upper-left of col in same row.
   for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)) :
       if (board[r][c] == 'Q') :
           return False

   # Check if there is a queen 'Q' on the lower left of col in same row.
   for r, c in zip(range(row+1, len(board), 1), range(col-1, -1, -1)) :
      if (board[r][c] == 'Q') :
          return False

   return True

def PlaceAll (board) :
    for row in board :
        for val in row:
            print(val,end="   ")
        print()

def NQueensSolution (chessboard, col) :
    # If all the columns have a queen 'Q', solution has been found.
    global queenscnt

    if (col >= len(chessboard)) :
        queenscnt += 1
        print("\nBoard " + str(queenscnt)+" :")
        print("----"*col)
        PlaceAll(chessboard)
        print("===="*col)

    else :
        #Placing the queen in each row of the column and verify if its safe
        for row in range(len(chessboard)) :
            chessboard[row][col] = 'Q'

            if (IsSafe(chessboard, row, col) == True) :
                # Placing Queen safe hence, trying to place Q in the next column.
                NQueensSolution(chessboard, col + 1)

            # restore empty space as previously placed queen is not valid
            chessboard[row][col] = '.'


#Driver code
board = []
NSize = int(input("Enter chessboard size : "))
for i in range(NSize) :
   row = ["."] * NSize
   board.append(row)

# place the queen 'Q' from the 0'th column.
NQueensSolution(board, 0)