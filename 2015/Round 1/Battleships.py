# BATTLESHIPS

# Up and down are y coordinates, left and right are x
# To access correct coordinates, input board[y, x]
import pprint
board = [[False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False]]

# Change later to input
variables = input()
a, c, m = variables.split(" ")
a = int(a)
c = int(c)
m = int(m)
# Change later to 0
r = 0

def calc_r(a, c, m, r):
    r = int(((a*r)+c)%m)
    return r



def calc_xy(r):
    x = r%10
    y = int(((r%100 - x)/10))
    return x, y

def verticalHorizontal(r):
    if r % 2 == 0:
        return "H"
    else:
        return "V"

def validLength(x, y, ship_size, orientation):
    if orientation == "V":
        if (y+ship_size) <= len(board):
            return True
        else:
            return False
    else:
        if (x+ship_size) <= len(board):
            return True
        else:
            return False


def checkNeighbours(x, y, ship_size, orientation):
    if orientation == "V":

        for i in range(abs(ship_size-y)):
            try:
                if board[y+i][x] == True:
                    return True



                # Check if any spaces are occupied
                elif board[y+i][x] == True:
                    return True

                # Check for horizontal neighbours
                elif board[y+i][x+1] == True:
                    return True
                elif board[y+1][x-1] == True:
                    return True

                # Check for diagonal members at ends
                if board[y+ship_size+1][x+1] == True or board[y+ship_size+1][x-1] == True:
                    return True

                elif board[y-1][x+1] == True or board[y-1][x-1] == True:
                    return True
            except IndexError:
                pass

        else:
            return False


    if orientation == "H":
        for i in range(abs(ship_size-x)):
            try:
                # Check if any spaces are occupied
                if board[y][x+i] == True:
                    return True

                # Check for vertical neighbours
                elif board[y+1][x+i] == True:
                    return True
                elif board[y-1][x+i] == True:
                    return True

                # Check for diagonal members at ends
                if board[y+1][x+ship_size] == True or board[y-1][x+ship_size] == True:
                    return True

                elif board[y-1][x-1] == True or board[y+1][x-1] == True:
                    return True

            except IndexError:
                pass
            else:
                    return False


def validPlacement(x, y, ship_size, orientation):
    if not(board[y][x]):
        if validLength(x, y, ship_size, orientation):
            if not checkNeighbours(x, y, ship_size, orientation):
                return True


    return False












go_again = True




while go_again:
    r = calc_r(a, c, m, r)
    x, y = calc_xy(r)
    r = calc_r(a, c, m, r)
    orientation = verticalHorizontal(r)
    ship_size = 4

    if validPlacement(x, y, ship_size, orientation):


        if orientation == "V":
            for i in range(ship_size):

                board[y+i][x] = True
        else:
            for i in range(ship_size):

                board[y][x+i] = True

        output = []
        go_again = False

print(x, y, orientation)


for ship3 in range(2):
    go_again = True
    ship_size = 3

    while go_again:
        r = calc_r(a, c, m, r)
        x, y = calc_xy(r)
        r = calc_r(a, c, m, r)
        orientation = verticalHorizontal(r)

        if validPlacement(x, y, ship_size, orientation):


            if orientation == "V":
                for i in range(ship_size):

                    board[y+i][x] = True
            else:
                for i in range(ship_size):

                    board[y][x+i] = True

            output = []
            go_again = False

    print(x, y, orientation)


for ship2 in range(3):
    go_again = True
    ship_size = 2

    while go_again:
        r = calc_r(a, c, m, r)
        x, y = calc_xy(r)
        r = calc_r(a, c, m, r)
        orientation = verticalHorizontal(r)

        if validPlacement(x, y, ship_size, orientation):


            if orientation == "V":
                for i in range(ship_size):

                    board[y+i][x] = True
            else:
                for i in range(ship_size):

                    board[y][x+i] = True

            output = []
            go_again = False

    print(x, y, orientation)

for ship1 in range(4):
    go_again = True
    ship_size = 1

    while go_again:
        r = calc_r(a, c, m, r)
        x, y = calc_xy(r)
        r = calc_r(a, c, m, r)
        orientation = verticalHorizontal(r)

        if validPlacement(x, y, ship_size, orientation):


            if orientation == "V":
                for i in range(ship_size):

                    board[y+i][x] = True
            else:
                for i in range(ship_size):

                    board[y][x+i] = True

            output = []
            go_again = False

    print(x, y, orientation)
