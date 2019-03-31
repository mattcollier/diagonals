def check_neighbors(row, col, value):
    global grid

    # check left value
    if(col > 0):
        leftValue = grid[row][col - 1]
        if (leftValue != 0 and leftValue != value):
            return False

    if row > 0:
        pRow = grid[row - 1]

        # check above value
        above = pRow[col];
        if (above != 0 and above != value):
            return False

        # check aboveLeft
        if (value == 1 and col > 0):
            aboveLeft = pRow[col -1];
            if (aboveLeft != 0 and aboveLeft != -1):
                return False

        # check aboveRight
        if (value == -1 and col < size - 1):
            aboveRight = pRow[col + 1]
            if (aboveRight != 0 and aboveRight != 1):
                return False

    return True

def extend(row, col, remainingDiags):
    global size
    global grid

    if remainingDiags == 0:
        print('Solution:', grid)
        exit()

    if row == size:
        return

    nextRow = row
    nextCol = col + 1
    if nextCol == size:
        nextRow += 1
        nextCol = 0

    # putting -1 first here optimizes for the known solution
    # -1 is /, 1 is \, 0 is blank cell
    for diagonalType in [1, -1, 0]:
        # zero (blank cell) always works, no need to test
        if diagonalType == 0:
            grid[row][col] = diagonalType
            extend(nextRow, nextCol, remainingDiags)
        else:
            if check_neighbors(row, col, diagonalType):
                # the diagonal works, put it in
                grid[row][col] = diagonalType
                extend(nextRow, nextCol, remainingDiags - 1)


# setup a grid size X size
size = 5
grid = [[55 for i in range(size)] for j in range(size)]

extend(0, 0, 16)
