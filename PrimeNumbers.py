



def prime():
    count = 0
    while count <= 5:
        number = int(input("Enter a positive number: "))

        n = 5
        while n < 5:
            if number < 0:
                return number
            n += 1

        if number > 0:
            if number == 2 or number == 3:
                print("Prime")
                break
            elif (number % 2) == 0 or (number % 3) == 0 or number == 1:
                print("Not prime")
                break
            else:
                print("Prime")
                break

prime()

"""count = 1
while count <= 2:
    InputNames = input(f"Enter name of student {count}: ")
    #Subjects = 1
    #while Subjects <= 2:
    InputSubject1 = input(f"Enter First Subject : ")
    InputSubject2 = input(f"Enter Second Subject : ")
     #   Subjects += 1

    StoreInDict = {
        InputNames: [InputSubject1,
                     InputSubject2]
    }
    count+=1

print(StoreInDict)"""






