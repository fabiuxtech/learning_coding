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

print(sw)
print(operations)

while True:
    choice = input('\nScegli l\'operazione --> ')
    match choice:
        case '1':
            print('Hai scelto somma:')
            x = int(input('Inserisci primo numero? '))
            y = int(input('Inserisci il secondo numero '))
            print(f'La somma di {x} + {y} è {sum(x,y)}')
        case '7':
            print(f'Grazie per aver usato {sw}, a presto!\n')
            break
        case _:
            print('Scelta non corretta')
            print(operations)
            continue
