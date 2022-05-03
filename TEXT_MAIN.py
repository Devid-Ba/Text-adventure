from sys import exit

inventory = []

def welcome():
    print("Welcome to Text Adventure!")
    print("""A great evil has befallen the land, you're the only hero left that can 
         Stop the evil from spreading. Your first step will be to locate the evil wizards tower
         Good Luck Hero""")
    sign()
    
def sign():
    print("In front of you is a signpost")
    print("west. Old Grove Forest")
    print("east. Village")
    print("north. abandoned farm house")
    print("south. go back home.")
    print("Where would you like to go?")
    
    choice = input("> ")

    if  "east" in choice:
        print("You start walking towards the East, in front of you is a path that leads into a forest")
        forest()
    elif "west" in choice:
        print("You start walking west, in the distance you see a village")
        #village()
    elif "north" in choice:
        print("You make your way towards and abandoned farm house")
        #farm()
    elif "south" in choice:
        print("""Your cowardice has allowed evil to spread.
              You look foward to a life time of work in the mines,as civiliztion falls around you""")
        exit(0)
    else:
        print("I did not get that, please try again")
        sign()
     
     
        
def forest():
    print("the forest is covered in webs, they are too large to have been spun by a regular spider")
    print("As you walk through the forest you come at a fork on the road")
    print("west. The westward path is covered in webs")
    print("East. The eastward path is well worn by foot and horse traffic")
    print("Which way would you like to head?")
    
    choice = input("> ")

    if "west" in choice:
        print("You start making your way westword")
        print("All the webs make the path hard to navigate")
        spider()
    
def spider():
    print("As you make your way throug all the webs, you come face to face with a Giant spider")
    print("What do you do?")
    print("run foward. you try to push your way foward through the spider")
    print("run back. You attempt to mske your way to the fork in the forest road")
    print("fight. ypu fight the spiders")
    print("bribe.")
    spider_armed == False
    
    while True:
        choice = input("> ")

        if choice == "run foward":
            death("The Spider webs you and takes you into the trees never to be seen again")
        elif choice == "fight" and not spider_armed:
            print("You take out your sword and fight")
            print("you vanquished the Spider")
            spider_armed = True    





welcome()