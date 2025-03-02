#!/usr/bin/env python3
welcome = "Welcome to the User Casino Register Portal"
lines = "--------------------------------------------"
usersNumber = 0
usersList = []
nickname = ""
age = ""
genderList = ("M", "F", "m", "f")
i = 1

print(f"\n {welcome} \n")
print(f"{lines}")

def myUsers():
    for user in usersList:
        print(f"User Info:")
        for key,value in user.items():
            if key == "Games":
                joinG=','.join(value)
                print(f" {key}: {joinG.title()}")
            else:
                print(f" {key}: {value}")
        print("\n")

        
def reports():
    print(f"Now printing Reports\n")
    print(f"Users Stats:")
    print(f" Male Users: {calcMales(usersList):.2f}%")
    print(f" Female Users: {calcFemales(usersList):.2f}%")
    print(f"\nAge Stats:")
    print(f" Min Age: {doMin(usersList)}")
    print(f" Max Age: {doMax(usersList)}")
    print(f" Mean Age: {doMean(usersList,'Age'):.2f}")
    print(f"\nNickname Stats:")
    print(f" Mean Nickname Length: {doMean(usersList,'Nickname'):.2f}")
    pass

def calcMales(x):
    males = 0
    for user in x:
        if user["Gender"] in ("M", "m"):
            males += 1
    males = (males / len(x)) * 100
    return males

def calcFemales(x):
    females = 0
    for user in x:
        if user["Gender"] in ("F", "f"):
            females += 1
    females = (females / len(x)) * 100
    return females

def doMin(x):
    min = x[0]["Age"]
    for user in x:
        if user["Age"] < min:
            min = user["Age"]
    return min

def doMax(x):
    max = x[0]["Age"]
    for user in x:
        if user["Age"] > max:
            max = user["Age"]
    return max

def doMean(x,y):
    mean = 0
    for user in x:
         if y == "Age":
            mean += user[y]
         elif y == "Nickname":
            mean += len(user[y])
    mean = mean / len(x)
    return mean

try:
    try:
        usersNumber = int(input("\nInsert the number of users you want to register: "))
    except ValueError:
        print(f"\n Invalid number\n")
    while i <= usersNumber:
            breakpoint = False
            print(f"\nInsert User {i} details ")
            try:
                nickname=input("\n Insert your nickname: ")
                for user in usersList:
                    if nickname in user["Nickname"]:
                        breakpoint = True
                        print("\n Nickname already in use") 
                        break
                if breakpoint:
                    continue
                print(f" Nickname is: {nickname}")
                age=int(input("\n Insert your age: "))
                if age < 18:
                    print(f"\n You're {age} so you are not allowed to enter the Casino\n")
                    continue
                elif age not in range(18, 101):
                    print(f"\n {age} is an invalid age\n")
                    continue
                print(f" Age is: {age}")
            except ValueError:
                print(f"\n Invalid age\n")
                continue
            gender=input("\n Insert your gender (M/F): ").capitalize()
            if gender not in genderList:
                print("\n Invalid gender")
                continue
            print(f" Gender is: {gender}")
            games=input("\n Insert the games you want to play separated by comma: ")
            usersList.append({"Nickname": nickname, "Age": age, "Gender": gender, "Games": games.split(", ")})
            
            if i == usersNumber:
                print(f"{lines}\n")
                print(f"Printing all users...which are {len(usersList)}\n")
                myUsers()
                print(usersList[0]["Games"])
                print(f"All users added! Thank you for your time!\n")
                print(f"{lines}\n")
                if usersNumber > 1:
                    reports()
            else:
                print(f"\nUser n.{i} added!\n\nGo with the next one...\n")
                print(f"{lines}\n")
            i += 1
except KeyboardInterrupt:
    print(f"\n\nProgram interrupted, you pressed CTRL+C\n")
    exit(1)