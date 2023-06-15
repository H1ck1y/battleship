def a_int(string:str)->bool:
    """
    check if the sting is a integer
    :param string: the input string
    :return: bool value, if the string is a integer
    """
    return string.isdigit()

def negative(string:str)->bool:
    """
    check if the string is a nagative integer
    :param string:the input string
    :return: bool value, if the string is a nagetive value
    """
    if string[0] == '-':
        return False
    else:
        return True

def  getvalidinputrow():
    """
    get the rownumber for the board
    :return: the row number
    """
    rown = input("Enter the number of rows:")
    rown = rown.strip()
    while not (a_int(rown) and negative(rown)):
        rown = input("Enter the number of rows:")
        rown = rown.strip()
    return int(rown)


def getvalidinputcol():
    """
    get the colume number of the board
    :return: the colume number
    """
    coln = input("Enter the number of columns:")
    coln = coln.strip()
    while not (a_int(coln) and negative(coln)):
        coln = input("Enter the number of columns:")
        coln = coln.strip()
    return int(coln)


def getvalidinputpiecetowin():
    """
    the number of piece to win
    :return: return the number of piece to win
    """
    np = input("Enter the number of pieces in a row to win:")
    np = np.strip()
    while not (a_int(np) and negative(np)):
        np = input("Enter the number of pieces in a row to win:")
        np = np.strip()
    return int(np)


def getvalidcolumndrop(c):
    """
    make sure the colume you drop is on the board
    :param c:the colume you drop
    :return: the colume you drop
    """
    cd = input("Enter the column you want to play in:")
    cd = cd.strip()
    flag = False
    while not flag == True:
        if a_int(cd) == True:
            cd = int(cd)
            if cd <= c-1:
               flag = True
               return cd
            else:
               cd = input("Enter the column you want to play in:")
               cd = cd.strip()
        else:
            cd = input("Enter the column you want to play in:")
            cd = cd.strip()


def makeboard(r,c):
 """
 make the board
 :param r:number of row
 :param c: number of columes
 :return: the board
 """
 board = []
 for rows in range(r):
    row = []
    for columes in range(c):
     row.append('*')
    board.append(row)
 return board

def printboard(a,c,r):
 """
 print the board
 :param a:board
 :param c: number of columes
 :param r: number of row
 :return: no return just printing the board
 """
 print(end='  ')
 for header in range(c):
     print(header,end = ' ')
 print()
 for row_index , row in enumerate(a):
     print((r-1-(row_index)),' '.join(row))

def findtherow(a,r,cd):
    """

    :param a:board
    :param r: row number
    :param cd: the colume you drop
    :return: the row you drop
    """
    for row in range (r-1,-1,-1):
        if a[row][cd] == '*':
            return row

def dropthepiece(a,row,cd,piecesymbol):
    """

    :param a:board
    :param row: the row you drop
    :param cd: the
    :param piecesymbol:
    :return:
    """
    a[row][cd] = piecesymbol


def horizontalwin(a,r,c,p,symbol):
    """
    check for horizontal win
    :param a:board
    :param r:the row number
    :param c:the colume number
    :param p:the the piecenumber you need to win
    :param symbol:the symbol of player
    :return: bool value
    """
    for cn in range(c+1-p):
        for rn in range(r):
         if a[rn][cn:cn+p:1]==[symbol]*p:
             return True

def verticalwin(a,r,c,p,symbol):
    """
    check for vertical win
    :param a: board
    :param r: the row number
    :param c: the colume number
    :param p: the the piecenumber you need to win
    :param symbol: the symbol of player
    :return:  bool value
    """
    a = list(zip(*a))
    tuple = (symbol,)
    for cn in range(c+1-p):
        for rn in range(r):
          if (a[rn][cn:cn+p:1]) == tuple*p:
              return True


def leftdiagol(a,r,c,p,symbol):
 """
 check for leftdiagnol win
 :param a: board
 :param r: the row number
 :param c: the colume number
 :param p: the piecenumber you need to win
 :param symbol: the symbol of the player
 :return: bool value
 """
 col2 = c
 for i in range(r):
    for j in range(col2-1, -1,-1):
        lst=[]
        i1,j1 = i,j
        while i1 <= r - 1 and j1 <= c-1:
            lst.append(a[i1][j1])
            j1 = j1 + 1
            i1 = i1 + 1
        if lst.count(symbol) == p:
            return True
        if i == 0 and j ==0:
            col2 = 1

def rightdiagol(a,r,c,p,symbol):
 """
 check for rightdiagnol win
 :param a:  board
 :param r:  rownumber
 :param c:  columenumber
 :param p: the number of piece you need to win
 :param symbol: the symbol of the player
 :return: bool value
 """
 k=0
 for i in range(r):
    for j in range(k,c):
        lst=[]
        i1,j1 = i,j
        while i1 <= r - 1 and j1 >=0:
            lst.append(a[i1][j1])
            j1 = j1 - 1
            i1 = i1 + 1
        if lst.count(symbol) == p:
            return True
        if i == 0 and j == c-1:
            k = c - 1

def main():
 """
 play the game
 :return:
 """
 r = getvalidinputrow()
 c = getvalidinputcol()
 p = getvalidinputpiecetowin()
 a = makeboard(r, c)
 printboard(a,c,r)
 turn = 0
 number = 0
 gameover = False
 while not gameover == True or number == r*c:
   try:
    if turn == 0:
        cd = getvalidcolumndrop(c)
        roww = findtherow(a, r, cd)
        dropthepiece(a, roww, cd, "X")
        printboard(a,c,r)
        if horizontalwin(a,r,c,p,'X') == True or verticalwin(a,r,c,p,'X')== True or leftdiagol(a,r,c,p,'X') == True or rightdiagol(a,r,c,p,'X') == True:
            gameover = True
            print("Player 1 won!")
            break

    if turn == 1:
        cd = getvalidcolumndrop(c)
        roww = findtherow(a, r, cd)
        dropthepiece(a, roww, cd, "O")
        printboard(a,c,r)
        if horizontalwin(a,r,c,p,'O') == True or verticalwin(a,r,c,p,'O')== True or leftdiagol(a,r,c,p,'O') == True or rightdiagol(a,r,c,p,'O') == True:
            gameover = True
            print("Player 2 won!")
            break
   except TypeError:
       continue
   turn = turn + 1
   turn = turn % 2
   number = number + 1
   if number == r*c:
        print("Tie Game")
        break

main()



