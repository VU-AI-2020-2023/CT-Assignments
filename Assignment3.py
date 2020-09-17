
while True:
    number = int(input("Number of people to invite: "))

    if number > 6:
        print("Too many, try again!")
    else:
        for i in range(number):
            name = str(input("Name of person: "))
            print("%s inivted!" % name)
        break
