#Calcolo MCD e m.c.m tra 2 numeri
def mcd(a,b):
    while b:
        if a == b:
            break
        a, b = b, a % b
    return a
def mcm(a,b):
    c = a * b / mcd(a,b)
    return c
def getNum():
    a=input(f"Inserire primo numero: ")
    b=input(f"Inserire secondo numero: ")
    if a.isnumeric() and b.isnumeric():
        a=int(a)
        b=int(b)
        return a,b
    else:
        print("Devi inserire solo numeri")
def printMCD():
    num=list(getNum())
    print(f"\nIl M.C.D. tra {num[0]} e {num[1]} è {mcd(num[0],num[1])}\n")
def printMCM():
    num=list(getNum())
    print(f"\nIl m.c.m. tra {num[0]} e {num[1]} {mcm(num[0],num[1])}\n")
def keepGoing():
    keepG=input(f"\nVuoi continuare? S/N -> ")
    keepG=keepG.lower()
    if keepG == "s" or keepG == "n":
        return keepG
    else:
        print("\nScelta non valida, inserire S per si N per no\n")
        keepGoing()
while True:
    mess="""
    Che operazione vuoi fare? (scegliere il numero corrispondente)
    1 -> Calcolo del Massimo Comune Divisore
    2 -> Calcolo del Minimo Comune Multiplo
    3 -> Uscire
    """
    print(mess)
    choice=input("Inserisci qui la scelta --> ")
    if choice.isnumeric():
        choice=int(choice)
    else:
        print("\nScelta non valida")
        continue
    match choice:
        case 1:
            printMCD()
            keepG=keepGoing()
            if keepG == "s":
                continue
            else:
                print(f"\nExiting...")
                break
        case 2:
            printMCM()
            keepG=keepGoing()
            if keepG == "s":
                continue
            else:
                print(f"\nExiting...")
                break
        case 3:
            print("\nExiting...")
            break
        case _:
            print(f"\nScelta non valida")
            continue