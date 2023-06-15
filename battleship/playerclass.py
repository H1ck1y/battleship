class player:
    """
    this class define the behaviour of the class
    """
    def __init__(self,r,c,pb,ps,fb,name):
        self.placementboard = pb
        self.fireboard = fb
        self.row = r
        self.col = c
        self.piecesymbol = ps
        self.name = name


    def makeplacementboard(self):
     """
     this function make the placement board
     :return: return the placement board
     """
     for rows in range(self.row):
        row = []
        for columes in range(self.col):
            row.append('*')
        self.placementboard.append(row)
     return self.placementboard

    def makefireboard(self):
        """
        this function make the fireboard
        :return: the fireboard
        """
        for rows in range(self.row):
            row = []
            for columes in range(self.col):
                row.append('*')
            self.fireboard.append(row)
        return self.fireboard

    def ppalcementboard(self):
        """
        this function print the placement board
        :return: no return value
        """
        print(f"{self.name}'s Placement Board")
        print(end='  ')
        for header in range(self.col):
            print(header, end=' ')
        print()
        for row_index, row in enumerate(self.placementboard):
            print((row_index), ' '.join(row))

    def printfireboad(self):
        """
        this function print the fireborad
        :return: no return value
        """
        print(f"{self.name}'s Firing Board")
        print(end='  ')
        for header in range(self.col):
            print(header, end=' ')
        print()
        for row_index, row in enumerate(self.fireboard):
            print((row_index), ' '.join(row))

    def droptheshiphorizontal(self,rp,cp,shiplength):
        """
        this function drop the ship horizontally
        :param rp: row position
        :param cp: colume position
        :param shiplength: the shiplenghlisit
        :return: the placement board
        """
        counter = 0
        while not counter == shiplength:
         self.placementboard[rp][cp+counter] = self.piecesymbol
         counter = counter + 1
        return self.placementboard

    def droptheshipvertial(self,rp,cp,shiplength):
        """
        this function drop the ship verticlaly
        :param rp: row position
        :param cp: colume position
        :param shiplength: the shiplength
        :return: placement board
        """
        counter = 0
        while not counter == shiplength:
          self.placementboard[rp+counter][cp] = self.piecesymbol
          counter = counter+1
        return self.placementboard

    def checkhvaliddrop(self,rp,cp,shiplength):
        """
        this function check if the horizontaldrop is valid
        :param rp: row position
        :param cp: colume position
        :param shiplength: shiplengh
        :return: bool value
        """
        if rp >= 0 and cp >= 0:
           if rp <= self.row-1 and (cp + shiplength-1) <= self.col-1:
               if  self.placementboard[rp][cp:cp+shiplength:1] == ['*'] * shiplength:
                   return True
               else :
                   return False
           else :
               return False
        else:
            return False

    def checkvvaliddrop(self,rp,cp,shiplength):
        """
        check if the vertical drop is valid
        :param rp: row position
        :param cp: colume position
        :param shiplength: shiplengh
        :return: bool value
        """
        if rp >= 0 and cp >=0:
            if cp <= self.col-1 and (rp + shiplength-1) <= self.row-1:
               if list(zip(*self.placementboard))[cp][rp:rp+shiplength:1] == ('*',)*shiplength:
                    return True
               else:
                    return False
            else:
                return False
        else:
             return False

    def checkvvalidfire(self,fr,fc):
        """
        check valid fire position
        :param fr: fire row position
        :param fc: fire colume position
        :return: bool value
        """
        lst = ['X', 'O']
        if fr >= 0 and fc >= 0:
            if fr <= self.row - 1 and fc <= self.col - 1:
                if self.fireboard[fr][fc] in lst:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False


    def markfireboard(self,symbol,firerowposition,firecolumnposition):
        """
        mark the fire position
        :param symbol: the symbol used to mark
        :param firerowposition: fire row position
        :param firecolumnposition: fire cilumeposition
        :return: fire board
        """
        self.fireboard[firerowposition][firecolumnposition] = symbol
        return self.fireboard

    def destroyshiponplacementboard(self,symbol,firerowpositon,firecolumnposition):
        """
        change the placementborad
        :param symbol: the firesymbol
        :param firerowpositon: firerowposition
        :param firecolumnposition: firecolume position
        :return: the new placement borad
        """
        self.placementboard[firerowpositon][firecolumnposition] = symbol
        return self.placementboard

    def judgeforhit(self,fr,fc,n1,n2):
        """
        judge wheather hit a ship
        :param fr: firerow position
        :param fc: firecolume position
        :param n1: name1
        :param n2: name2
        :return: bool value
        """
        list1 = ['*','X','O']
        if self.placementboard[fr][fc] in list1:
            print(f"{n1} missed.")
            return False
        else:
            print(f"{n1} hit {n2}'s {self.placementboard[fr][fc]}!")
            return True


    def checkforwin(self):
        """
        check the board and find who win the game
        :return: bool value
        """
        number1 = sum(x.count('*') for x in self.placementboard)
        number2 = sum(x.count('X') for x in self.placementboard)
        number3 = sum(x.count('O') for x in self.placementboard)
        total = number1 + number2 + number3
        if total == self.row * self.col:
            return True
        else:
            return False

    def checkfordestroytheship(self,fr,fc,n1,n2):
        """
        check if a ship is destroyed by a player
        :param fr: firerow position
        :param fc: firecolume position
        :param n1: name1
        :param n2: name2
        :return: print the result
        """
        shipsymbol = self.placementboard[fr][fc]
        number = sum(x.count(shipsymbol) for x in self.placementboard)
        if number == 1:
            print(f"{n1} destroyed {n2}'s {shipsymbol}!")
        else:
            return None

