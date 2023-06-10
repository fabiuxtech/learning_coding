#!/usr/bin/python
# This is a Test file for learning purpose
#import keyword
#print(keyword.kwlist)
#for k in keyword.kwlist:
#    print(k,end='\n')
print('Hi!\nWhat\'s your name?')
name = input()
print(f'Nice to meet you {name}')
while True:
    print('Are you enjoying the course? (Yes/No)')
    enj = input()
    enj = enj.lower()
    if enj == 'yes':
        print('Glad to hear that')
        break
    elif enj == 'no':
        print('Sorry to hear that')
        break
    else:
        print(f'Word {enj} not accepted')
        continue