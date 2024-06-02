#!/bin/python3
# adv-project v0.1
# author: Fabio Carrassi
land = "project-land"
<<<<<<< HEAD
invent = []
=======
invent = {"cookies"}
>>>>>>> 359dbcfc0f7b432086a3b2d6ea11ff1902b8a7b5
where = ""
s = "sud"
n = "nord"
e = "east"
w = "west"
h = "help"
inv = "inventory"
wami = "lost"
def exiting():
    pass
class iNventory:
    def __init__(self) -> None:
        pass
    def empty():
        print(f"Inventory is empty")
    def full():
        print(f"Inventory is Full")
    def listing():
        print(f"Those are your items:")
<<<<<<< HEAD
    #to complete
    def relitem(item):
        print(f"Want to trash {item}? y/n ")
        choice = input(f"=> ")
        choice == lower(choice)
        if choice == "y":
            invent.remove(item)
            return choice
        else:
            print(f"No item released")
            return choice
    def takeitem(item):
        pass
=======
        print(invent)
>>>>>>> 359dbcfc0f7b432086a3b2d6ea11ff1902b8a7b5
def inventory():
    if invent == {}:
        print(f"Your inventory is: empty")
    else:
        print(f"Your inventory is: {invent}")
def backtoprompt():
    print(f"What's your next move?")
    choices(input(f"=> "))
def choices(where):
    wami = "no-where"
    where = str.lower(where)
    match where:
        case "h":
            print(f"""
                  This is help section...
                  Your available choices:
                    s = {s}
                    n = {n}
                    e = {e}
                    w = {w}
                    i = {inv}
                    h = {h}
                    where = To know here you are
                  """)
            choices(input(f"=> "))
        case "i":
            if invent == []:
                iNventory.empty()
                backtoprompt()
            elif invent == "Full":
                iNventory.full()
                backtoprompt()
            else:
                iNventory.listing()
                backtoprompt()
        case "s":
            print(f"You're going {s}...")
            wami = s
            backtoprompt()
        case "where":
            print(f"You're {wami}")
            backtoprompt()
        case "exit":
            exit
        case _:
            backtoprompt()
print(f"Welcome to {land}\nType 'h' for {h}")
backtoprompt()