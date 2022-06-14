def placeQueen(r, c, brd):
    for y in range(c):
        if brd[r][y] != '+':
            return False

    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if brd[i][j] != '+':
            return False

    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if brd[i][j] != '+':
            return False
    return True


def placed():
    for q in queens:
        if queens[q] == [-1, -1]:
            return False
    return True


def showBoard(b):
    print()
    for x in range(n):
        for y in range(n):
            print(b[x][y], end="  ")
        print()


def tryQueen(c, brd):
    if c >= n:
        return True
    for row in range(n):
        x = "Q"+str(c+1)
        if placeQueen(row, c, brd):
            queens[x] = [row, c]
            brd[row][c] = row+1
            tryQueen(c+1, brd)
            if placed():
                showBoard(brd)
                queens[x] = [-1, -1]
                if placeQueen(row, c, brd):
                    brd[row][c] = '+'
            brd[row][c] = '+'
    return False


n = int(input("Enter the number of queens: "))
cbrd = [['+' for i in range(n)] for j in range(n)]
queens = {}
for i in range(n):
    x = "Q"+str(i+1)
    queens[x] = [-1, -1]
tryQueen(0, cbrd)
