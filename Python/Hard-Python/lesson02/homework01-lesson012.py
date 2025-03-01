#!/usr/bin/env python3
# list1=[2, 4, 6, 8, 10]
# list2=[3, 5, 7, 9, 11]
list1=[]
list2=[]
for i in range(5):
    list1.append(int(input("Inserisci un numero per la lista 1: ")))
    list2.append(int(input("Inserisci un numero per la lista 2: ")))
list3=list1+list2
print(list3)