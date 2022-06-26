def showPos():
    print()
    for i in bank:
        x = "Bank "+i
        mis = bank[i][0]
        can = bank[i][1]
        print(x, ":", mis, "M and", can, "C")


def isValid(b):
    mis, can = bank[b][0], bank[b][1]
    if ((mis < can) & (mis != 0)):
        return False
    return True


def mov(m, c, b):
    bank[b][0] -= m
    bank[b][1] -= c
    f1 = isValid(b)
    for i in bank:
        if i != b:
            bank[i][0] += m
            bank[i][1] += c
            f2 = isValid(i)
    bank["A"][2], bank["B"][2] = bank["B"][2], bank["A"][2]
    return (f1 & f2)


def isWin():
    for i in bank["A"][:2]:
        if i != 0:
            return False
    return True


def menu():
    flag = True
    while flag:
        if(bank['A'][2]):
            bnk = 'A'
        else:
            bnk = 'B'

        l = bank[bnk]
        flM, flC, flB = True, True, True
        print("\nBoat is at Bank", bnk)
        while flB:
            while flM:
                m = int(input("Number of missionaries to move (0 for none): "))
                if (m > l[0]) | (m > 2):
                    print("\nEnter Valid input")
                else:
                    flM = False
            while flC:
                c = int(input("Number of cannibals to move (0 for none): "))
                if (c > l[1]) | (c > 2):
                    print("\nEnter Valid input")
                else:
                    flC = False
            if m+c > 2:
                print("\nThe boat can hold max 2")
                flM, flC = True, True
            elif m+c == 0:
                print("\nThe boat has to hold min 1")
                flM, flC = True, True
            else:
                flB = False
        flag = mov(m, c, bnk)
        showPos()
        if not flag:
            return flag
        if isWin():
            return True


bank = {
    'A': [3, 3, True],
    'B': [0, 0, False]
}
showPos()
F = menu()
if F:
    print("\nMission Successful!!")
else:
    print("\nGame Over!!")
