from math import sqrt

sw = 'Calculator 1.0'

def sum(x,y):
    tot = x + y
    return tot

def sub(x,y):
    tot = x - y
    return tot

def mult(x,y):
    tot = x * y
    return tot

def div(x,y):
    tot = x / y
    return tot

def power(num,x=1):
    tot = 1
    for n in range(x):
        tot *= num
    return tot

def square(x):
    tot = sqrt(x)
    return tot

def isNumber(x,y='1'):
    if x.isdigit() and y.isdigit():
        return 0
    else:
        return 1

def stringToNumber(x,y='1'):
    x = int(x)
    y = int(y)
    return x,y

def pause():
    x = input('Vuoi continuare? (S/N)')
    x = x.lower
    if x == 's':
        return x
    elif x == 'n':
        return x
    else:
        return x
    
operations = '''
    Scegli l'operazione:
    1) Somma
    2) Sottrazione
    3) Moltiplicazione
    4) Divisione
    5) Elevamento a potenza
    6) Radice quadrata
    7) Esci dal programma
    '''

print('\n',sw)
print(operations)

while True:
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
                print(f'La somma di {sTn[0]} + {sTn[1]} è {sum(sTn[0],sTn[1])}')
        case '2':
            print('Hai scelto Sottrazione:')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'La differenza tra {sTn[0]} - {sTn[1]} è {sub(sTn[0],sTn[1])}')
        case '3':
            print('Hai scelto Moltiplicazione')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'Il risultato tra {sTn[0]} * {sTn[1]} è {mult(sTn[0],sTn[1])}')
        case '4':
            print('Hai scelto Divisione:')
            x = input('Inserisci il primo numero: ')
            y = input('Inserisci il secondo numero: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'Il risultato di {sTn[0]} : {sTn[1]} è {div(sTn[0],sTn[1])}')
        case '5':
            print('Hai scelto Elevamento a Potenza:')
            x = input('Inserisci il numero da elevare: ')
            y = input('Inserisci l\'esponenente: ')
            if isNumber(x,y) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x,y)
                print(f'Il risultato di {sTn[0]} elevato a {sTn[1]} è {power(sTn[0],sTn[1])}')
        case '6':
            print('Hai scelto Radice Quadrata:')
            x = input('Inserisci il numero sul quale calcolare la radice quadrata: ')
            if isNumber(x) == 1:
                print(f'\nDevi inserire solo numeri\nHai inserito {x} e {y}')
            else:
                sTn = stringToNumber(x)
                print(f'La radice quadrata di {sTn[0]} è {sqrt(sTn[0])}')
        case '7':
            print(f'\nGrazie per aver usato {sw}, a presto!\n')
            break
        case _:
            print('Scelta non corretta')
            print(operations)
            continue
