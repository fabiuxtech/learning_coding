#!/usr/bin/python3
import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D':13, 'E': 14, 'F': 15 
}


#Funzione di conversione esadecimale ==> decimale
def hexToDec(hexNum):
    numLenght = len(hexNum)
    i = numLenght - 1
    decNum = 0
    power = 0
# Metodo 1 
    while i >= 0:
        #print(hexNumbers[hexNum[i]])
        print(power)
        decNum += hexNumbers[hexNum[i]] * (16 ** power)
        #print(decNum)
        i -= 1
        power += 1
    return decNum

# Metodo 2
    # for char in hexNum[::-1]:
    #    single_char = hexNumbers.get(char)
    #    decNum += single_char * (16 ** power) 
    #    power += 1
    # return decNum

hexNum = input(f'\nInserisci il numero esadecimale: ')
print(f'Il decimale di {hexNum} è: {hexToDec(hexNum):n}')

#Varie Prove
#print(f'\n{hexNum} in decimale è: {hexToDec(hexNum)}\n')

#print(f'\nIl numero {hexNum} contiene {numlenght} cifre')
#if numlenght <= 3:
#    hexToDec
#    print(f'Le singole cifre sono:')
#    for num in range(0,numlenght):
#        print(hexNum[num])
#else:
#    print(f'\n{hexNum} contiene più di 3 cifre non posso convertirlo.')