#!/bin/python3
from math import sqrt

sw = "Calculator 1.3"
helloM = "Benvenuto su {}".format(sw)
byeM = "Grazie per aver usato {}, a presto!".format(sw)
firstStart = 0

def sum(x,y):
    tot = x + y
    return tot

# # TEST somma di N argomenti
# def bigSum(a):
#     operators = ["+"]
#     tot = 0
#     for i in a:
#         print(i,end=" ")
#         if i != operators:
#             if i.isdigit():
#                 tot += int(i)
#     print("=",end=" ")
#     return tot
# a="3+1+2+3"
# print(bigSum(f"\n{a}"))
# # FINE TEST

def sub(x,y):
    tot = x - y
    return tot

def mult(x,y):
    tot = x * y
    return tot

def div(x,y):
    if y == 0:
        return "Non si può dividere per zero"
    else:
        tot = x / y
        return tot

# def power(num,x=1):
#     tot = 1
#     for n in range(x):
#         tot *= num
#     return tot

def power(num,x=1):
    tot = 1
    i = x
    while i >= 1:
        tot *= num
        i -= 1
    return tot

def square(x):
    tot = sqrt(x)
    return tot

def isNumber(x,y):
    if x.isdigit() and y.isdigit():
        return 0
    else:
        return 1

def stringToNumber(x,y='1'):
    x = int(x)
    y = int(y)
    return x,y
    
operations = '''
    Queste le operazioni a tua disposizione:
    1) Somma
    2) Sottrazione
    3) Moltiplicazione
    4) Divisione
    5) Elevamento a potenza
    6) Radice quadrata
    7) Esci dal programma
    '''

print(f"\n", helloM)

while True:
    if firstStart == 0:
        print(operations)
        firstStart = 1
    else:
        keepGoing=input(f'\nDesideri continuare con le operazioni? (S/N) --> ')
        keepGoing = keepGoing.lower()
        if keepGoing == 's':
            print(operations)
        elif keepGoing == 'n':
            print(f'\n{byeM}\n')
            break
        else:
            print(f'\nRisposta non corretta.')
            continue
    choice = input('\nScegli l\'operazione --> ')
    print('\n')
    match choice:
        case '1':
            print('Hai scelto Somma:')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nLa somma di {sTn[0]} + {sTn[1]} è {sum(sTn[0],sTn[1])}')
        case '2':
            print('Hai scelto Sottrazione:')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nLa differenza tra {sTn[0]} - {sTn[1]} è {sub(sTn[0],sTn[1])}')
        case '3':
            print('Hai scelto Moltiplicazione')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nIl risultato tra {sTn[0]} * {sTn[1]} è {mult(sTn[0],sTn[1])}')
        case '4':
            print('Hai scelto Divisione:')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nIl risultato di {sTn[0]} : {sTn[1]} è {div(sTn[0],sTn[1])}')
        case '5':
            print('Hai scelto Elevamento a Potenza:')
            x = input('Inserisci il numero da elevare: ')
            y = input('Inserisci l\'esponenente: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nIl risultato di {sTn[0]} elevato a {sTn[1]} è {power(sTn[0],sTn[1])}')
        case '6':
            print('Hai scelto Radice Quadrata:')
            x = input('Inserisci il numero sul quale calcolare la radice quadrata: ')
            y = "1"
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'\nLa radice quadrata di {sTn[0]} è {sqrt(sTn[0])}')
        case '7':
            print(f'\n{byeM}\n')
            break
        case _:
            print('Scelta non corretta')
            continue