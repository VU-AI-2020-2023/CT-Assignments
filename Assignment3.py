# Problem 7

while True:
    guests = int(input("Number of people to invite: "))

    if guests > 6:
        print("Too many, try again!")
    else:
        for i in range(guests):
            guest_name = str(input("Name of person: "))
            print("%s inivted!" % guest_name)
        break
