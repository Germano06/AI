def showJugs():
    volA = jugs['a'][1]
    volB = jugs['b'][1]
    jA = "A("+str(jugs['a'][0])+")"
    jB = "B("+str(jugs['b'][0])+")"
    print("\nThe contents of the jug are:\n")
    print("|".ljust(7), "|   |", "|".rjust(7))
    print("|", str(volA).center(5), "|   |", str(volB).center(5), "|")
    print("-".center(9, "-"), " ", "-".center(9, '-'))
    print(jA.center(9), "   ", jB.center(6))


def decision(d):
    if d == 1:
        if jugs['a'][1] == vA:
            print("\nJug A is already full")
            return False
        jugs['a'] = [vA, vA]

    if d == 2:
        if jugs['a'][1] == 0:
            print("\nJug A is already empty")
            return False
        jugs['a'] = [vA, 0]

    if d == 3:
        if jugs['b'][1] == vB:
            print("\nJug B is already full")
            return False
        oldVolA = jugs['a'][1]
        oldVolB = jugs['b'][1]

        if oldVolA > vB-oldVolB:
            newVolA = oldVolA-(vB-oldVolB)
            newVolB = oldVolB+(oldVolA-newVolA)
        else:
            newVolA = 0
            newVolB = oldVolB+oldVolA
        jugs['a'] = [vA, newVolA]
        jugs['b'] = [vB, newVolB]

    if d == 4:
        if jugs['b'][1] == vB:
            print("\nJug B is already full")
            return False
        jugs['b'] = [vB, vB]

    if d == 5:
        if jugs['b'][1] == 0:
            print("\nJug B is already empty")
            return False
        jugs['b'] = [vB, 0]

    if d == 6:
        if jugs['a'][1] == vA:
            print("\nJug A is already full")
            return False
        oldVolA = jugs['a'][1]
        oldVolB = jugs['b'][1]
        if oldVolB > vA-oldVolA:
            newVolB = oldVolB-(vA-oldVolA)
            newVolA = oldVolA+(oldVolB-newVolB)
        else:
            newVolA = oldVolB+oldVolA
            newVolB = 0
        jugs['b'] = [vB, newVolB]
        jugs['a'] = [vA, newVolA]
    return True


def menu():
    ch = 1
    count = 0
    maxMov = 20
    while (ch != 0):
        print("\n1-> Fill Jug A")
        print("2-> Empty Jug A")
        print("3-> Pour Jug A into Jug B")
        print("4-> Fill Jug B")
        print("5-> Empty Jug B")
        print("6-> Pour Jug B into Jug A")
        print("0-> Exit")
        ch = int(input("Enter your choice: "))
        while (ch > 6) | (ch < 0):
            ch = int(input("Enter a valid choice: "))
        if decision(ch):
            showJugs()
            count += 1
            print("\nMoves left ->", maxMov-count)
            if ((jugs['a'][1] == n) | (jugs['b'][1] == n)):
                return True
            if count == maxMov:
                print("Out of moves")
                return False
    return False


jugs = {
    'a': [],
    'b': []
}
vA = int(input("Enter the volume of Jug A: "))
jugs['a'] = [vA, 0]
vB = int(input("Enter the volume of Jug B: "))
jugs['b'] = [vB, 0]
n = int(input("Enter the final volume needed: "))
showJugs()
flag = menu()
if(flag):
    print("\nSuccessfully Completed the Game!!")
else:
    print("\nGame Over!!")
