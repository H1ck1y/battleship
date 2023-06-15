def printHangman(hang):
  """
  this function help us draw the hangman
  :param hang: record the number of failing times
  :return:  have no return value, just return the graph
  """
  if hang == 0:
      return None
  if hang == 1:
      print(' | ')
  if hang == 2:
      print(' | ')
      print(' 0 ')
  if hang == 3:
      print(' | ')
      print(' 0 ')
      print(' | ')
  if hang == 4:
      print(' | ')
      print(' 0 ')
      print('/| ')
  if hang == 5 :
      print(' | ')
      print(' 0 ')
      print('/|\ ')
  if hang == 6 :
      print(' | ')
      print(' 0 ')
      print('/|\ ')
      print('/')
  if hang == 7:
      print(' | ')
      print(' 0 ')
      print('/|\ ')
      print('/ \\')


def checkforwhitespace(word):
    """

    :param word: the word
    :return: return if the word contains space or ?
    """
    word = word.strip()
    flag = True
    for i in range(0,len(word)):
        if word[i] == ' ' or word[i] == '?' :
            flag = False
    return flag

def getvalidinput():
    """

    :return: get the valid input for the guessedword
    """
    secret = input('Please enter a word to be guessed\nthat does not contain ? or white space:')
    valid = False
    while not valid == True:
         secret = secret.strip()
         if checkforwhitespace(secret) == True:
             valid = True
             return secret
         else:
             valid = False
             secret = input('Please enter a word to be guessed\nthat does not contain ? or white space:')

secretword = getvalidinput()


def showcorrect(guessedword,cg,letter):
    """
    this function replace * when guess correctly
    :param guessedword: the word player guessed
    :param cg: cypher version of guess number
    :param letter: the letter you guessed
    :return: return the new version
    """
    index = 0
    new = ''
    for i in guessedword:
        if i == letter:
            new = new + letter
        elif cg[index] != '*':
            new = new + cg[index]
        else:
            new = new + '*'
        index = index + 1
    return new


def getvalidletter():
    """
    this function works for getting the valid input for the letter you guessed
    :return:the letter you guessed each time
    """
    le = input("Please enter your next guess:")
    check = False
    while not check == True:
        le = le.strip()
        le = le.lower()
        if len(le) == 1:
            check = True
        if len(le) > 1:
            print("You can only guess a single character.")
            le = input("Please enter your next guess:")
            check = False
        if le == '':
            print('You must enter a guess.')
            le = input("Please enter your next guess:")
    return le


def main(guessedword,hang = 0):
    """
    this function is the main fuction, combine all the function together

    :param guessedword: the word you want to guess
    :param hang: the number of failing times
    :return: no return value, this is main function
    """
    lst= []
    cg = "?" * len(guessedword)
    print(cg)
    win = False

    while not hang == 7 :
        print("So far you have guessed:" + ((',').join(str(x)for x in lst)))
        letter = getvalidletter()
        while letter in lst:
            print("You already guessed the character:",letter)
            letter = getvalidletter()
        if letter in guessedword:
            cg = showcorrect(guessedword,cg,letter)
            printHangman(hang)
        else:
            hang = hang + 1
            printHangman(hang)
        number = cg.count("?")
        if number == 0:
            print("You correctly guessed the secret word:",guessedword)
            break
        elif hang == 7:
            print("You failed to guess the secret word:",guessedword)
        else:
            print(cg)
        lst.append(letter)
        lst.sort()

main(secretword,hang=0)