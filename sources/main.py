from follow import Follow
from monster import Monster
from physics import Physics
from player import Player

def main():
    print("welcome to this simple monster fighting game")
    print("monsters will find your position and come towards you")
    print("when they are close enough, attack\n ")

    gamePlaying = True
    numAlive = 3
    player = Player()
    mon1 = Monster()
    mon1.position = [10,10,10]
    mon2 = Monster()
    mon2.position = [20,20,20]
    mon3 = Monster()
    mon3.position = [5,5,5]
    movement = [-5,-5,-5]
    physics = Physics()
    follow = Follow()
    i = 0
   # monsters = [mon1, mon2, mon3]

    while gamePlaying:
        print("\n*****************************************")
        print('you are at [0,0,0]')
        print('you have',player.numAttacks, 'attacks left')
        print('the monsters are at ')


        #print pos
        if mon1.checkAlive():
            print(*mon1.position, sep = ", ")
        if mon2.checkAlive():
            print(*mon2.position, sep=", ")
        if mon3.checkAlive():
            print(*mon3.position, sep=", ")
        print("\n... monsters moving ... \n")
        i +=1

        # attacking
        choice = input("attack? Y/N: ")
        if choice == 'Y':
            player.numAttacks -= 1
            which = input("which monster: ")
            print("\n*****************************************\n")
            if which == "1":
                if follow.closeEnough(mon1.position, player.position) and mon1.checkAlive():
                    mon1.damage()
                    print("you killed a monster!")
                    numAlive -= 1
                else:
                    print("you can't attack that one too bad")
            if which == "2":
                if follow.closeEnough(mon2.position, player.position) and mon2.checkAlive():
                    mon2.damage()
                    print("you killed a monster!")
                    numAlive -= 1
                else:
                    print("you can't attack that one too bad")
            if which == "3":
                if follow.closeEnough(mon3.position, player.position) and mon3.checkAlive():
                    mon3.damage()
                    print("you killed a monster!")
                    numAlive -= 1
                else:
                    print("you can't attack that one too bad")
        elif choice == 'N':
            print("no attack used")
        else:
            print("wasted turn on invalid entry smh")

        #updating pos
        if not follow.closeEnough(mon1.position, player.position):
            mon1.position = physics.update_position(movement, mon1.position, 1)
        if not follow.closeEnough(mon2.position, player.position):
            mon2.position = physics.update_position(movement, mon2.position, 1)
        if not follow.closeEnough(mon3.position, player.position):
            mon3.position = physics.update_position(movement, mon3.position, 1)

        if numAlive == 0 or player.numAttacks == 0:
            gamePlaying = False

    if numAlive == 0:
        print("\n*****************************************")
        print("congrats you killed them all!")
    else:
        print("\n*****************************************")
        print("ran out of attacks - there are", numAlive, "monsters left")
        print("better luck next time")

if __name__ == '__main__':
    main()
