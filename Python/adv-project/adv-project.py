#!/bin/python3
# adv-project v0.1
# author: Fabio Carrassi
land = "project-land"
invent = {}
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
def inventory():
    if invent == {}:
        print(f"Your inventory is: empty")
    else:
        print(f"Your inventory is: {invent}")
def backtoprompt():
    print(f"What's your next move?")
    choices(input(f"=> "))
def choices(where):
    wami = "lost"
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
            if invent == {}:
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
print(f"Welcome to {land}\nType 'h' for {h}")
backtoprompt()