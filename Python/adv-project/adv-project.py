# adv-project v0.1
# author: Fabio Carrassi
land="project-land"
invent={}
where=""
s = "sud"
n = "nord"
e = "east"
w = "west"
h = "help"
inv = "inventory"
def exiting():
    pass
def inventory():
    if invent == {}:
        print(f"Your inventory is: empty")
    else:
        print(f"Your inventory is: {invent}")
def backtoprompt():
    print(f"What's your next move? > ")
    choices(input())
def choices(where):
    where = str.lower(where)
    match where:
        case "h":
            print(f"""This is help section...
                  Your available choices:
                    s = {s}
                    n = {n}
                    e = {e}
                    w = {w}
                    i = {inv}
                    h = {h}
                  """)
            choices(input())
        case "i":
            inventory()
        case "s":
            print(f"You're going {s}...")
print(f"Welcome to {land}\nType 'h' for {h}")
backtoprompt()