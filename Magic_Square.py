

# taking a input, and converting it to an integer
N = int(input('Please enter N: '))

# checking weather N is odd or greater than 0, if not enter another N
while(N<=0 or N%2==0):
    N = int(input('Please enter correct N (Must be odd and greater than 0: '))

# Calculation of the sum of each column, Row or diagonal
MagicSquare = N*(N**2 + 1)/2

# Making a magic square matrix for a valid N
Square = [[0] * N for _ in range(N)]        # Putting 0's in an N by N matrix
Coordinate = lambda col, row: (N * ((col + row - 1 + int(N/2))% N) + ((col + 2*row - 2) % N) + 1)      # Moving to the right co ordinates  en.wikipedia.org/wiki/magic_square
for col in range(N):                        # looping N times columns
    for row in range(N):                    # looping N times rows
        Square[col][row] = Coordinate(col + 1, row + 1)      # putting values into the matrix
        

for rw in range(N):
    print(*Square[rw], sep='\t')

# Testing the magic square if it's valid or not
def Valid():
    # checking the sum of every item in a row if its equal to MagicSquare number
    for item in range(N):
        assert sum(Square[item]) == MagicSquare
        
    # checking the sum of diagonal from top-left corner to bottom-right corner
    assert sum(Square[i][i] for i in range(N)) == MagicSquare
    
    # checking the sum of diagonal from top-right corner to bottom-left corner
    assert sum(Square[i][N-i-1] for i in range(N)) == MagicSquare
    
    # exchanging the columns and rows
    transposedSquare = [[Square[rw][cl] for rw in range(N)] for cl in range(N)]
    # checking the sum of columns, which are rows now
    for item in range(N):
        assert sum(transposedSquare[item]) == MagicSquare
    return True

# finding if the magic square is correct or not
if(Valid()):
    print('Correct')
else:
    print('Incorrect')
