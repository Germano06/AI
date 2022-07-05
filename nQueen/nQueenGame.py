def placeQueen(r, c, brd):
    for row in range(r):
        if brd[row][c] != '+':
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if brd[i][j] != '+':
            return False

    for i, j in zip(range(r, -1, -1), range(c, n)):
        if brd[i][j] != '+':
            return False
    return True


def showBoard(b):
    print()
    for x in range(n):
        for y in range(n):
            print(b[x][y], end="  ")
        print()


def placed():
    for q in queens:
        if queens[q] == [-1, -1]:
            return False
    x = True
    for r in range(n):
        for c in range(n):
            x = placeQueen(r, c, cbrd)
            if not x:
                break
        if not x:
            break
    return x


def undoMove(r, b):
    x = "Q"+str(r+1)
    queens[x] = [-1, -1]
    for c in range(n):
        b[r][c] = '+'
    queens['turn'] = True


def putQueen(row, col, brd):
    x = "Q"+str(row+1)
    queens[x] = [row, col]
    brd[row][col] = row+1


def getColumn(row, brd):
    fl, fCol = False, True
    if queens['turn']:
        print("\nEnter column to place the queen in row", row+1, ":", end=" ")
        while fCol:
            col = int(input())
            if col <= n:
                fCol = False
            else:
                print("\nEnter valid input:")
        col -= 1
        fl = placeQueen(row, col, brd)
        putQueen(row, col, brd)
    else:
        print("\nComputer to place queen in row", row+1)
        for c in range(n):
            if placeQueen(row, c, brd):
                fl = True
                putQueen(row, c, brd)
                break
    return fl


def tryQueen(row, brd):
    while ((not placed()) & (row < n)):
        f = getColumn(row, brd)
        showBoard(brd)
        if not f:
            print("\nFurther progress not possible!!")
            if queens['turn']:
                ch = input("Do you want to undo? (y for yes): ")
                if ch == 'y':
                    undoMove(row, brd)
                    if row-1 >= 0:
                        row -= 1
                        undoMove(row, brd)
                else:
                    return False
            else:
                print("Undoing the move")
                undoMove(row-1, brd)
                row -= 2
                undoMove(row, brd)
            showBoard(brd)
        else:
            queens['turn'] = not queens['turn']
            row += 1
    return True


n = int(input("Enter the number of queens: "))
cbrd = [['+' for i in range(n)] for j in range(n)]
queens = {
    'turn': True
}
for i in range(n):
    x = "Q"+str(i+1)
    queens[x] = [-1, -1]
f = tryQueen(0, cbrd)
if f:
    print("\nCompleted!!!")
else:
    print("\nGame over!!")
