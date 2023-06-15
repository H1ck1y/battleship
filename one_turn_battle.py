

def crioccur(cripro):
    """

    :param cripro: the probability of critical hit
    :return: if it is a cirtical hit
    """
    if cripro >= random.random():
        return True

    else:
        return False


def hitland(landpro):
    """

    :param landpro: the probability of hit accurately
    :return: if it hits accurately
    """
    if landpro >= random.random():
        return True
    else:
        return False

def dodge(dodgepro):
    """

    :param dodgepro: the probability of defender dodge
    :return: if it dodges
    """
    if dodgepro >= random.random():
        return True
    else:
        return False

def attack(strenth,cripro,landpro,dodpro):
    """

    :param strenth: the strengh of the hit
    :param cripro: the probability of critical hit
    :param landpro: the probability of hit accurately
    :param dodpro: the provavility of dodge
    :return: return the damage of hit
    """
    if crioccur(cripro) == True:
        damage = strenth + 1
        print('attacker crit defender for',damage,'points of damage')
    else:
        if hitland(landpro) == True:
            if dodge(dodpro) == True:
                damage = 0
                print("defender dodged attacker's attack")

            else:
                damage = random.randint(strenth // 2 , strenth)
                print("attacker hit defender for",damage, "points of damage")
        else:
            print("attacker missed defender")
            damage = 0
    return damage


def counterattack(strenth,cripro,landpro,dodpro):
    """

    :param strenth: the strengh of the hit
    :param cripro: the probability of critical hit
    :param landpro: the probability of hit accurately
    :param dodpro: the provavility of dodge
    :return: return the damage of hit
    """
    if crioccur(cripro) == True:
        damage2 = strenth + 1
        print('defender crit attacker for',damage2,'points of damage')
    else:
        if hitland(landpro) == True:
            if dodge(dodpro) == True:
                damage2 = 0
                print("attacker dodged defender's attack")

            else:
                damage2 = random.randint(strenth // 2 , strenth)
                print("defender hit attacker for",damage2, "points of damage")
        else:
            print("defender missed attacker")
            damage2 = 0
    return damage2

def guarding():
    if guard == 'Y':
        return True
    if guard == 'n':
        return False




import random
s = int(input("Enter the seed to run the fight with:"))
random.seed(s)
ahp = int(input("Enter the attacker's hp:"))
attackstrength = int(input("Enter the attacker's strength:"))
alandpro = (float(input("Enter the attacker's accuracy:")))/100
acripro = (float(input("Enter the attacker's crit chance:")))/100
adodpro = (float(input("Enter the attacker's dodge rate:")))/100
dhp = int(input("Enter the defender's hp:"))
defendstrength = int(input("Enter the defender's strength:"))
dlandpro = (float(input("Enter the defender's accuracy:")))/100
dcripro = (float(input("Enter the defender's crit chance:")))/100
ddodpro = (float(input("Enter the defender's dodge rate:")))/100
guard = input("Is the defender guarding? Y for yes, n for no: ")
destroy = attack(attackstrength,acripro,alandpro,ddodpro)
if destroy < dhp or destroy == 0 or guarding() == True:
    destroy2 = counterattack(defendstrength, dcripro, dlandpro, adodpro)
else:
    destroy2 = 0
m1 = ahp - destroy2
if m1 < 0:
    m1 = 0
m2 = dhp - destroy
if m2 < 0:
    m2 = 0
print('After fighting the attacker has',m1,'hp left and the defender has',m2,'hp left')


