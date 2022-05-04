class GameExit(Exception):

    """The game as concluded."""


def ask_user(*options):
    """Accept user input."""
    while True:
        choice = input("> ")
        if choice in options:
            return choice
        else:
            print(f"{choice!r} is not a valid choice")


def welcome(state):
    print("Welcome to Text Adventure!")
    print("""A great evil has befallen the land, you're the only hero left that can
         Stop the evil from spreading. Your first step will be to locate the evil wizards tower
         Good Luck Hero""")
    return sign, state


def sign(state):
    print("In front of you is a signpost")
    print("east. Old Grove Forest")
    print("west. Village")
    print("north. abandoned farm house")
    print("south. go back home.")
    print("Where would you like to go?")

    match ask_user("east", "west", "north", "south"):
        case "east":
            print("You start walking towards the East, in front of you is a path that leads into a forest")
            return forest, state
        case "west":
            print("You start walking west, in the distance you see a village")
            return #village, state
        case "north":
            print("You make your way towards and abandoned farm house")
            return #farm, state
        case "south":
            raise GameExit("""Your cowardice has allowed evil to spread.\nYou look foward to a life time of work in the mines,as civiliztion falls around you""")


def forest(state):
    print("the forest is covered in webs, they are too large to have been spun by a regular spider")
    print("As you walk through the forest you come at a fork on the road")
    print("west. The westward path is covered in webs")
    print("East. The eastward path is well worn by foot and horse traffic")
    print("Which way would you like to head?")

    choice = ask_user("west")

    if "west" in choice:
        print("You start making your way westword")
        print("All the webs make the path hard to navigate")
        return spider, state


def spider(state):
    print("As you make your way throug all the webs, you come face to face with a Giant spider")
    print("What do you do?")
    print("run foward. you try to push your way foward through the spider")
    print("run back. You attempt to mske your way to the fork in the forest road")
    print("fight. ypu fight the spiders")
    print("bribe.")

    choice = ask_user("run forward", "fight")

    if choice == "run foward":
        raise GameExit("The Spider webs you and takes you into the trees never to be seen again")
    elif choice == "fight" and not state.get("spider armed"):
        print("You take out your sword and fight")
        print("you vanquished the Spider")
        state["spider armed"] = True
        return #XXX, state
    else:
        raise GameExit("XXX")


def main():
    """Start the event loop."""
    state = {}  # The way the world is.
    tick = welcome  # A single step updating the world.
    try:
        while True:
            tick, state = tick(state)
    except GameExit as exc:
        print(exc)
        # Exit the program.
        return


if __name__ == "__main__":
    main()
welcome()
