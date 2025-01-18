import random as rm
import os
AI = ['bag', 'hammer', 'scissors']
lv = [int(i) for i in range(2, 6, 2)]
w = []
file = open('PYTHON\\Test\\tree.txt', 'r', encoding='utf-8-sig')
r = file.readline()
while r != "":
    w.append(str(r).strip('\n'))
    r = file.readline()
file.close()
point = [0, 0]
data = [0, 7, 0, 5000]
level = [0]
key = ''
g, g1 = [], {}
memory = [0, 0]
__human__ = [
    """

     _______
----'  _____)_____
            ______)__
  human     _________)     
            _______)
----._____________)        """,
    """
     _______
----'  _____)__
        (______)
  human (_______)
        (______)
----.____(____) """,
    """
     _________
----'    _____)____
           ________)_
  human _____________)
       (______)
----.__(_____)"""]
__AI__ = [
    """
          _________
    _____(______   '---
 __(________
(___________     ai
  (_________
   (_______________.---""",
    """
     _______
  __(_____  '---
 (_____)
(______)   ai
 (_____)
  (____)_____.---""",
    """
        _________
   ____(_____    '---
 _(_________       
(____________     ai
       (______)
        (_____)__.---"""]


def screen():

    print(f'''
    ===========================================================
    |                  Write code game is easy                |
    |                                                         |
    |                   MY TOPIC = MYCI TOP                   |
    |                                                         |
    |                   YOUR CREDIT: {data[3]}$                      |
    ===========================================================''')
    print()
    print(' '*15, 'WELCOME TO GAME OF THE WORLD')
    print()
    name = input('Name player : ')
    print()
    name_friend = input('Name computer : ')
    print()
    memory[0], memory[1] = name, name_friend
    print(' '*18, 'Hello _%s_ and _%s_' % (name, name_friend))
    print()
    print("""   
    ===========================================================
    |Note : You have to choice [HAMMER] - 1 ,[SCISSORS] - 2 or|
    |[BAG] - 0.If you stop the game,please choice [EXIT] - 3  |
    | Please choice [Continue]-4 or [Setting]-5 if you don't  |
    |        want.Thank you for reading ;)                    | 
    |               IF YOU WIN,YOU HAVE your place bet        |
    |               IF YOU LOSE,YOU LOSE your place bet       |
    |               ONLY APPLY TO DIFFERENT LEVEL!!!          |
    =========================================================== """)
    print()
    print(' '*20, "LET'S GO !!!")
    print()

    # =======================================================

    while True:
        l = input(
            'LV computer : \n  >>> 1-Normal \n  >>> 2-Different \n  >>> 3-Master \nSelect level : ')
        if l == '1' or l == '2' or l == '3':
            level[0] = int(l)
            break
        else:
            print(' '*18, 'PLEASE TRY AGAIN!!!')
    return ""


def main(l):
    if l == 1:
        while True:
            try:
                human = int(input('Your choice : '))
                point[0] += 1
                if int(human) == 3:
                    return exit()
                if int(human) == 4:
                    continue
                if int(human) == 5:
                    print(SETTING_GAME(l))
                if human == 0:
                    print(f"""{__human__[0]}{__AI__[1]}""")
                if human == 1:
                    print(f"""{__human__[1]}{__AI__[2]}""")
                if human == 2:
                    print(f"""{__human__[2]}{__AI__[0]}""")
                print(' '*22, f'You <===> {memory[1].upper()}')
                print(' '*13, f'SCORE : ___{point[0]}___:___{point[1]}___')
                print()
                print(' '*15, 'You win,good job !')
            except (ValueError, IndexError):
                print(' '*18, 'Xin hay nhap [0],[1],[2] !')
                return main(l)

     # ===========================================================

    if l == 2:
        while True:
            try:
                bet = int(input('Your bet : '))
                human = int(input('Your choice : '))
                ai = rm.choice(AI)
                if human == 3:
                    return exit()
                if human == 4:
                    continue
                if human == 5:
                    print(SETTING_GAME(l))

              # IF DRAW
                if AI[human] == ai:
                    print("""%s%s                """ %
                          (__human__[human], __AI__[AI.index(ai)]))
                    print(' '*22, f'You <===> {memory[1].upper()}')
                    print(' '*13, f'SCORE : ___{point[0]}___:___{point[1]}___')
                    print()
                    print(' '*15, 'DRAW , You strong !!!')
            except (ValueError, IndexError):
                print(' '*18, 'Xin hay nhap [0],[1],[2]')
                print()
                return main(l)

            # IF PLAYER WIN
            if (human == 0 and ai == AI[1]) or (human == 1 and ai == AI[2]) or (human == 2 and ai == AI[0]):
                data[3] += bet
                print("""%s%s                """ %
                      (__human__[human], __AI__[AI.index(ai)]))
                point[0] += 1
                print(' '*22, '{a} <===> {b}'.format(a='You',
                      b=memory[1].upper()))
                print(
                    ' '*13, 'SCORE : ___{c}___:___{d}___'.format(c=point[0], d=point[1]))
                print()
                print(' '*15, 'You win,good job !')
                print(' '*15, "You have %s$" % (bet))

              # IF AI WIN
            if (human == 1 and ai == AI[0]) or (human == 2 and ai == AI[1]) or (human == 0 and ai == AI[2]):
                data[3] -= bet
                print("""%s%s""" % (__human__[human], __AI__[AI.index(ai)]))
                point[1] += 1
                print(' '*22, f'You <===> {memory[1].upper()}')
                print(' '*13, f'SCORE : ___{point[0]}___:___{point[1]}___')
                print()
                print(' '*15, f'{memory[1]} win !!!')
                print('You lose %s$' % (bet))

    if l == 3:
        iq = rm.choice(lv)
        while iq >= 0:
            try:
                human = int(input('Your choice : '))
            except (ValueError, IndexError):
                print(' '*18, 'Xin hay nhap [0],[1],[2] !')
                return main(l)
            if human == 3:
                return exit()
            if human == 4:
                continue
            if human == 5:
                print(SETTING_GAME(l))
            if human == 0:
                print("""%s%s""" % (__human__[0], __AI__[2]))
            if human == 1:
                print("""%s%s""" % (__human__[1], __AI__[0]))
            if human == 2:
                print("""%s%s""" % (__human__[2], __AI__[1]))
            point[1] += 1
            print(' '*22, f'You <===> {memory[1].upper()}')
            print(' '*13, f'SCORE : ___{point[0]}___:___{point[1]}___')
            print()
            print(' '*18, '%s win !!!' % memory[1])
            iq -= 1
            if iq == 5:
                print(' '*18, 'HEY,BRO!!!')
                question = input('Do you want continue : ')
                if question.lower() == 'no':
                    return SETTING_GAME(l)
                else:
                    continue

     # =======================================================


def SETTING_GAME(l):
    print('List : \n >>> 1.Edit name \n >>> 2.Reset point \n >>> 3.Select level \n >>> 4.Restore game')
    e = int(input('Select number : '))
    if e == 1:
        e1 = int(
            input('Edit : \n >>> 1.Your name \n >>> 2.Computer name \n >>>Select number : '))
        if e1 == 1:
            memory[0] = input('Enter new your name : ')
            print(f'New name : {memory[0]} ')
        elif e1 == 2:
            memory[1] = input('Enter new computer name : ')
            print(f'New name : {memory[1]} ')
        return main(l)
    if e == 2:
        q3 = input('Are you sure ? : ')
        if q3.lower() == 'yes':
            point[0], point[1] = 0, 0
            print()
            print(' '*18, 'THE POINT HAD BEEN RESETED')
            print()
        else:
            print(' '*15, 'Happy to play game ;)')
        return main(l)
    if e == 3:
        e1 = input('The point will be deleted.Are you sure?\n>>>[Y/N] : ')
        if e1.lower() == 'y':
            l = int(input(
                'LV computer : \n  >>> 1-Normal \n  >>> 2-Different \n  >>> 3-Master \nSelect level : '))
            level[0] = l
            point[0], point[1] = 0, 0
        return main(l)
    if e == 4:
        point[0], point[1] = 0, 0
        level[0] = 0
        memory[0], memory[1] = 0, 0
        return screen()
    return main(l)
    # ========================================================


def exit():
    print(' '*15, 'Would you like save the point ?')
    q = input('Y/N : ')
    if q.lower() == 'y':
        print(' '*15, 'Would you like see point ?')
        q1 = input('Y/N: ')
        if q1.lower() == 'y':
            print('='*50)
            print()
            print("""                  %s | %s""" % ('YOU', 'YOUR FRIEND'))
            print("""                  %s : %s""" % (point[0], point[1]))
        print('='*50)
        print(' '*15, 'Thank You For playing game !')
    return False

# =====================================================

# HANG MAN


def __data__():
    data[0] = str(rm.choice(w))  # name
    data[2] = len(data[0])  # heart


def Screen():
    print("""
==============================
||    //                     |
||   //                      |
||  //                       | 
|| //        ________________|________________  
||//        |     Wellcome back to show       |
|//         |      game programming is        |
|/          |           [  EASY  ]            |
||          |     ! pay and let's play(laugh:)|
||          -----------------------------------
||
||
||
||
||
||
||
||           
||
||
||========================================================
||    #  #   #   #   #  ###      #   #   #   #   #      ||
||    #  #  # #  ##  # #         ## ##  # #  ##  #      ||
||    #### ##### # # # #  ##     # # # ##### # # #      ||
||    #  # #   # #  ## #   #     #   # #   # #  ##      ||
||    #  # #   # #   #  ####     #   # #   # #   #      ||
||                                                      ||
||    TRAINING YOUR BRAIN       TRAINING YOUR VOCABULARY||
==========================================================
""")
    print("""
    ---->OPTION : 
        >>>1. HINT [You are %s hint]
        >>>2. RESTART 
        >>>3. END GAME
        >>>4. BUY HINT
        HEART : you are %s heart
        $$$SPECIAL ,YOU HAVE %s$ COIN AND 1 HINT WILL TO PAY 100$
        """ % (data[1], data[2], data[3]))
    print()
    print("""                   LET'S GO !!!!.               """)
    for i in range(len(data[0])):
        if data[0][i] == " ":
            g.append(' ')
            g1.setdefault(i, data[0][i])
        else:
            g.append('_')
            g1.setdefault(i, data[0][i])
    return ""


def run():
    print("""         WORD     [""", end="")
    for j in g:
        print(j, end='')
    print("""]""")
    print('\r')
    print()
    global heart
    while '_' in g:
        print()
        word = str(input(""">>>Your letter : """))
        print()
        if word == '1':
            return hint()
        if word == '2':
            g.clear()
            g1.clear()
            data[1], data[3] = 7, 5000
            __data__()
            return Screen(), Main()
        if word == '3':
            return False
        if word == '4':
            return sell_hint()
        if word in data[0]:
            if word not in list(g1.values()):
                print(' '*18, f"Letter '{word}' already ixist")
                print()
                return Main()
            else:
                for j in list(g1.keys()):
                    if g1[j] == word:
                        g[j] = word
                        del g1[j]
                        break
                print("""         WORD     [""", end="")
                for j in g:
                    print(j, end='')
                print("""]""")
                print('\r')
                print()
        elif (word not in data[0]) or word == "":
            data[2] -= 1
            print()
            print(' '*18, 'WRONG LETTER')
            print(' '*18, f'You are {data[2]} heart ')
            print()
            if data[2] == 0:
                print(lose())
                print()
                print(f"""FULL WORDS :           [ {data[0]} ]""")
                print()
                q = input("""DO YOU WANT TO CONTINUE ?
>>>1. Yes
>>>2. No 
>>>""")
                if q == '1':
                    g.clear()
                    g1.clear()
                    __data__()
                    return __clear__(), Screen(), Main()
                else:
                    return False
            else:
                return run()
    print(win())
    print("""FULL WORDS :           [ %s ]""" % data[0])
    print()
    q = input("""DO YOU WANT TO CONTINUE ?
>>>1. Yes
>>>2. No 
>>>""")
    if q == '1':
        g.clear()
        g1.clear()
        __data__()
        return __clear__(), Screen(), Main()
    else:
        return False
    return False


def hint():
    data[1] -= 1
    if data[1] >= 0:
        h = str(rm.choice(list(g1.values())))
        if h == ' ':
            return hint()
        print()
        print(' '*18, 'KEY WORD IS : [%s]' % h)
        print()
        print(' '*18, 'YOU HAVE [%s] HINT' % data[1])
        print()
    else:
        print(' '*18, 'SORRY !! Out of suggestions')
    return Main()


def sell_hint():
    while True:
        buy = input("WOULD YOU LIKE BUY HINT[y/n]: ")
        if (buy.lower() != 'y') and (buy.lower() != 'n'):
            print("PLEASE TYPE [y] or [n] !!!")
        else:
            break
    if buy.lower() == "y":
        print("""LIST HINT:
             1. 1 hint - [100$]
             2. 5 hint - [500$]
             3. 10 hint - [1000$]
             4. 20 hint - [2000$]
             5. 50 hint - [5000$]""")
        while True:
            coin = input(">>>YOUR SELECT : ")
            if coin in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("PLEASE TYPE AGAIN !")
        if data[3] >= 100:
            if int(coin) == 1:
                data[3] -= 100
                data[1] += 2
            if int(coin) == 2 and data[3] >= 500:
                data[3] -= 500
                data[1] += 6
            if int(coin) == 3 and data[3] >= 1000:
                data[3] -= 1000
                data[1] += 11
            if int(coin) == 4 and data[3] >= 2000:
                data[3] -= 2000
                data[1] += 21
            if int(coin) == 5 and data[3] >= 5000:
                data[3] -= 5000
                data[1] += 51
            print("YOU HAVE A %s$ COIN LEFT AND %s HINT" % (data[3], data[1]))
            print()
        else:
            print("""SORRY,YOU HAVE %s$ COIN
            PLEASE PLAY THE 2ND GAME TO EARN MONEY""" % data[3])
    return run()


def Main():
    while run() == True:
        run()
    return """                   Thank you for playing !!!"""


def lose():
    print("""
                                    #       # ######  #      #
                                     #     # #      # #      #
                                      #   #  #      # #      #
                                       # #   #      # #      #
                                        #    #      # #      #
                                        #    #      # #      #
                                        #    #      # #      #
                                        #     ######   ######  
                
                                  #        ######   ###### ######
                                  #       #      # #       #
                                  #       #      # #       #
                                  #       #      #  #####  #####
                                  #       #      #       # #
                                  #       #      #       # #
                                  #######  ######  ######  ###### """)
    return ""


def win():
    print("""
                                    #       # ######  #      #
                                     #     # #      # #      #
                                      #   #  #      # #      #
                                       # #   #      # #      #
                                        #    #      # #      #
                                        #    #      # #      #
                                        #    #      # #      #
                                        #     ######   ######  
                                                      #
                                       #    #    #        #      #
                                       #    #    #    #   ##     #
                                       #    #    #    #   # #    #
                                       #    #    #    #   #  #   #
                                       #   # #   #    #   #   #  #
                                        # #   # #     #   #    # #
                                         #     #      #   #     ##""")
    return ""


def __clear__():
    os.system('clear')


def game():
    print("""GAME LIST : 
     >>> 1.Hang man
     >>> 2.Bag,scissors and hammer""")
    try:
        choice = int(input('Your choice : '))
    except ValueError:
        print('Please type [1] or [2]')
        return game()
    if choice == 1:
        __data__()
        Screen()
        Main()

    elif choice == 2:
        screen()
        while True:
            if main(level[0]) != False:
                main(level[0])
            else:
                break
    else:
        print('Please type [1] or [2]')
        return game()
    ques = input("""Do you want continue playing ?
    + 1.Y
    + 2.N
    >>>>>YOUR ANSWER [1/2] : """)
    if ques == '1':
        g.clear()
        g1.clear()
        return game()
    else:
        print("""
                         SEE YOU AGAIN ;)""")
        return ""


if __name__ == "__main__":
    game()
print(__human__[0])
