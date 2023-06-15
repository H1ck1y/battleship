from battleship.fileconfiguration import *
from battleship.playerclass import *

def getvaliddirectionandposition(shipname,shiplength,name,p,i):
    """
    get valid oreientation and position
    :param shipname: the name of the ship
    :param shiplength: the length of the ship
    :param name: the player name
    :param p: the player name
    :param i: the index of the shiplist
    :return: the direction and position you want to fire
    """
    a = input(f"{name}, enter the orientation of your {shipname}, which is {shiplength} long: ")
    a = a.lower()
    a = a.strip()
    list1 = ['h','ho','hor','hori','horiz','horizo','horizon','horizont','horizonta','horizontal','horizontall','horizontally']
    list2 = ['v','ve','ver','vert','verti','vertic','vertica','vertical','verticall','vertically']
    direction = None
    valid = False
    rp = None
    cp = None
    while not valid == True:
      try:
        if a in list1:
            direction = 'h'
            rp,cp= map(lambda x:int(x),input(f"Enter the starting location for your {shipname}, which is {shiplength} long, in the form row col: ").split())
            if p.checkhvaliddrop(rp,cp,shiplength=shiplenthlist[i])==True:
               valid = True
               break
            else:
                a = input(f"{name}, enter the orientation of your {shipname}, which is {shiplength} long: ")
                a = a.lower()
                a = a.strip()
                continue

        if a in list2:
            direction = 'v'
            rp, cp = map(lambda x: int(x), input(f"Enter the starting location for your {shipname}, which is {shiplength} long, in the form row col: ").split())
            if p.checkvvaliddrop(rp,cp,shiplength=shiplenthlist[i])==True:
               valid = True
               break
            else:
                a = input(f"{name}, enter the orientation of your {shipname}, which is {shiplength} long: ")
                a = a.lower()
                a = a.strip()
                continue
        else:
            a = input(f"{name}, enter the orientation of your {shipname}, which is {shiplength} long: ")
            a = a.lower()
            a = a.strip()
      except:
          a = input(f"{name}, enter the orientation of your {shipname}, which is {shiplength} long: ")
          a = a.lower()
          a = a.strip()
          continue
    return direction,rp,cp

def getthename():
    """
    get the name of the two player
    :return: two names
    """
    name1 = input("Player 1, please enter your name: ")
    name2 = input("Player 2, please enter your name: ")
    return name1, name2
path = input("Please enter the path to the configuration file for this game: ")
rownumber,colnumber,shipnumber,shiplists = readfile(path)
shipnamelist = getshipename(shiplists)
shiplenthlist = getshiplenth(shiplists)
name1,name2 = getthename()

def setupplayer1():
 """
 put the ship of player1 to the board
 :return: the placementboard
 """
 player1 = player(rownumber,colnumber,[],None,[],name1)
 board = player1.makeplacementboard()
 player1.ppalcementboard()
 for i in range(len(shipnamelist)):
    player1 = player(rownumber, colnumber, board, shipnamelist[i], [], name1)
    direction,rp,cp = getvaliddirectionandposition(shipnamelist[i],shiplenthlist[i],name1,player1,i)
    if direction == 'h':
        board = player1.droptheshiphorizontal(rp,cp,shiplenthlist[i])
        player1.ppalcementboard()
    if direction == 'v':
        board = player1.droptheshipvertial(rp,cp,shiplenthlist[i])
        player1.ppalcementboard()
 return board

def setupplayer2():
 """
 put the ship of player2 to the board
 :return: the placement board
 """
 player2 = player(rownumber,colnumber,[],None,[],name2)
 board = player2.makeplacementboard()
 player2.ppalcementboard()
 for i in range(len(shipnamelist)):
    player2 = player(rownumber, colnumber, board, shipnamelist[i], [], name2)
    direction, rp, cp = getvaliddirectionandposition(shipnamelist[i], shiplenthlist[i], name2,player2,i)
    if direction == 'h':
       board = player2.droptheshiphorizontal(rp, cp, shiplenthlist[i])
       player2.ppalcementboard()
    if direction == 'v':
            board = player2.droptheshipvertial(rp, cp, shiplenthlist[i])
            player2.ppalcementboard()
 return  board

def askforfirelocation(name,player):
     """
     this function asks for the fire location
     :param name: the player name
     :param player: the class name
     :return: return the firerowposition and firecolumeposition
     """
     a = input(f"{name}, enter the location you want to fire at in the form row col: ")
     flag = False
     while not flag == True:
      try:
        fr,fc = a.split()
        fr = int(fr)
        fc = int(fc)
        if player.checkvvalidfire(fr,fc) == True:
            flag = True
            return fr, fc
        else:
            a = input(f"{name}, enter the location you want to fire at in the form row col: ")
      except:
           a = input(f"{name}, enter the location you want to fire at in the form row col: ")
           continue


