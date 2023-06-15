from battleship.setupthegame import *
def playthegame():
 """
 two player plays the game, use the class
 :return: no return value, it is a procedure
 """
 board1 = setupplayer1()
 board2 = setupplayer2()
 player1play = player(rownumber,colnumber,board1,None,[],name1)
 fireboard1 = player1play.makefireboard()
 player2play = player(rownumber,colnumber,board2,None,[],name2)
 fireboard2 = player2play.makefireboard()
 gameover = False
 player1play.printfireboad()
 player1play.ppalcementboard()
 while not gameover == True:
    player1play = player(rownumber, colnumber, board1, None, fireboard1, name1)
    player2play = player(rownumber, colnumber, board2, None, fireboard2, name2)
    fr,fc = askforfirelocation(name1,player1play)
    if player2play.judgeforhit(fr,fc,name1,name2) == True:
        player2play.checkfordestroytheship(fr, fc, name1, name2)
        fireboard1 = player1play.markfireboard('X',fr,fc)
        board2 = player2play.destroyshiponplacementboard('X',fr,fc)
        if player2play.checkforwin() == False:
          player2play.printfireboad()
          player2play.ppalcementboard()
        else:
            player1play.printfireboad()
            player1play.ppalcementboard()
            print(f"{name1} won!")
            gameover = True
            break
    else :
        fireboard1 = player1play.markfireboard('O',fr,fc)
        board2 = player2play.destroyshiponplacementboard('O', fr, fc)
        player2play.printfireboad()
        player2play.ppalcementboard()
    fr,fc =askforfirelocation(name2,player2play)
    if player1play.judgeforhit(fr,fc,name2,name1) == True:
        player1play.checkfordestroytheship(fr, fc, name2, name1)
        fireboard2 = player2play.markfireboard('X',fr,fc)
        board1 = player1play.destroyshiponplacementboard('X',fr,fc)
        if player1play.checkforwin() == False:
           player1play.printfireboad()
           player1play.ppalcementboard()
        else:
            player2play.printfireboad()
            player2play.ppalcementboard()
            print(f"{name2} won!")
            gameover = True
            break
    else :
        fireboard2 = player2play.markfireboard('O',fr,fc)
        board1 = player1play.destroyshiponplacementboard('O', fr, fc)
        player1play.printfireboad()
        player1play.ppalcementboard()

