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
    print(f" Male Users: {calcGenders(usersList,"M"):.2f}%")
    print(f" Female Users: {calcGenders(usersList, "F"):.2f}%")
    print(f"\nAge Stats:")
    print(f" Min Age: {doMin(usersList)}")
    print(f" Max Age: {doMax(usersList)}")
    print(f" Mean Age: {doMean(usersList,'Age'):.2f}")
    print(f"\nNickname Stats:")
    print(f" Mean Nickname Length: {doMean(usersList,'Nickname'):.2f}")
    print(f"Favorite Games: {favGame()}")
    
def favGame():
    countGames = {}
    countFav = {"placeholder": 1}
    count = 1
    prevGame = 0
    favGame = ""
    for user in usersList:
        for game in user["Games"]:
            print(game,type(game))
            if game not in countGames:
                countGames.update({game: count})
            else:
                countGames.update({game: count+1})
    for key,value in countGames.items():
        if value > prevGame:
            countFav.popitem()
            countFav.update({key: value})
            # favGame = key,str(value)
        prevGame = value
    return countFav
def calcGenders(userList,gender):
    tot = 0
    for user in userList:
        if gender == "M":
            if user["Gender"] in ("M", "m"):
                tot += 1
        elif gender == "F":
            if user["Gender"] in ("F", "f"):
                tot +=1
    tot = (tot / len(userList)) * 100
    return tot

def doMin(userList):
    min = userList[0]["Age"]
    for user in userList:
        if user["Age"] < min:
            min = user["Age"]
    return min

def doMax(userList):
    max = userList[0]["Age"]
    for user in userList:
        if user["Age"] > max:
            max = user["Age"]
    return max

def doMean(userList,key):
    mean = 0
    for user in userList:
         if key == "Age":
            mean += user[key]
         elif key == "Nickname":
            mean += len(user[key])
    mean = mean / len(userList)
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
            usersList.append({"Nickname": nickname, "Age": age, "Gender": gender, "Games": games.split(",")})
            
            if i == usersNumber:
                print(f"{lines}\n")
                print(f"Printing all users...which are {len(usersList)}\n")
                myUsers()
                for user in usersList:
                    for game in user["Games"]:
                        print(game)
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