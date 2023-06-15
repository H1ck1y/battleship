from operator import itemgetter
def readfile(path):
    """
    this function open the file and read it
    :param path: the obsolute path of the file
    :return: return the rownumber,columenumber of the number, the shipnumber and shipinformation
    """
    with open(path, 'r') as file:
      rownumber = file.readline()
      rownumber = int(rownumber)
      colnumber = file.readline()
      colnumber = int(colnumber)
      shipnumber =file.readline()
      shipnumber = int(shipnumber)
      shiplists = []
      while True:
          oneship = file.readline().split()
          if not oneship:
              break
          shiplists.append(oneship)
      shiplists = sorted(shiplists,key=itemgetter(0))
    return rownumber,colnumber,shipnumber,shiplists


def getshipename(shiplists):
    """
    this function gets the shipname from the shiplist
    :param shiplists: the shiplists
    :return: the shipnamelist
    """
    shipnamelist = []
    for i in shiplists:
        shipnamelist.append(i[0])
    return shipnamelist

def getshiplenth(shiplists):
    """
    this function gets the shiplengh
    :param shiplists: the shiplists contain information
    :return: the shiplengh list
    """
    shiplenthlist = []
    for i in shiplists:
        shiplenthlist.append(i[1])
        shiplenthlist = [int(u) for u in shiplenthlist]
    return shiplenthlist


