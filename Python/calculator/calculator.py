from math import sqrt

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
        return 'continue'
    elif x == 'n':
        return 'break'
    else:
        print('Scelta non corretta')
    
    

operations = '''
Scegli l'operazione:
1) Somma
2) Sottrazione
3) Moltiplicazione
4) Divisione
5) Elevamento a potenza
6) Radice quadrata
'''

while True:
    print(operations)
    choice = input('--> ')
    # choice = int(choice)
    match choice:
        case '1':
            print('-- Hai scelto somma --')
            x = int(input('Inserisci primo numero: '))
            y = int(input('Inserisci secondo numero: '))
            print(f'La somma è: {sum(x,y)}')
            pause()