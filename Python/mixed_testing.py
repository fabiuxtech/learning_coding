games="1, 2, 3, 4"
print(games.split(","))

# word="Ramarro"
# letter=("r", "R")
# i=0
# total=0
# while i < len(word):
#     for char in word:
#         if char in letter:
#             total+=1
#         i+=1
#     print(total)

# my_list = [{}]
# my_list.append({"Name": "Fabio", "Age": 30, "Gender": "M"})
# print(my_list)
# print(type(my_list))

# def leftPad(stringa,lunghezza,carattere=1):
#     stringa = str(stringa)
#     i = -1
#     if carattere is not None and carattere != 0:
#         carattere = " "
#         lunghezza = lunghezza - len(stringa)
#         while i < lunghezza:
#             i += 1
#             stringa = carattere + stringa
#     return stringa
# print(leftPad("Ciao",5))

# my_string = "asdsdsndmsfdjfjdiorfemfdjkrdfmmnvmcvbniqopewrrituwencasnmdbnsmaaa"
# match = "r"
# counter = 0
# for char in my_string:
#     if match == char:
#         counter += 1
# print(f"Ho trovato {counter} caratteri '{match}' in 'my_string' ")    

# to_do = ["portare il cane a passeggio", "finire di studiare", "fare la spesa"]
# # print(f"\n".join(to_do))
# # for el in to_do:
# #     print(el)
# print(len(to_do))

# my_list = [9.81, "pasta", 13, 65, 3.14]
# new_list = ["asd", "ciccia", "pizza", my_list]
# print(new_list)
# print(new_list[3][-1]) # doppio indice per accedere indice di una lista dentro un'altra lista

# primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# match = 23
# print(f"Elenco numeri primi\n")
# for el in primi:
#     if el == match:
#         print(f"Num: {el} corrisponde al match --> {match}")
#     else:
#         print(f"Num: {el}")

#!/usr/bin/python
# This is a Test file for learning purpose
#import keyword
#print(keyword.kwlist)
#for k in keyword.kwlist:
#    print(k,end='\n')
#food = input('What\'s your favorite food? ')
#food = food.lower()
#if food == 'pizza':
#    print('Yep! So amazing!')
#else:
#    print('Yuck! That\'s not it!')
#print('Thanks for playing!')
# def favorite_city(name):
#     print('One of my favorite cities is', name)

# favorite_city('Roma')
# favorite_city('Tokyo')
# favorite_city('New York')

# def isEven(num):
#     return num % 2 == 0
# if isEven(3):
#     print('3 is even')
# else: 
#     print('3 is not even')
    
# a = "Python"
# b = "YtHo"
# if str.lower(b) in str.lower(a):
#     print(f"Yes {b} is in {a}")
# else:
#     print(f"No, {b} is not in {a}")
