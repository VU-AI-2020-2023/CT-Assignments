from datetime import date
from random import sample
from string import printable

def first():
    num1 = float(input("Give the first number: "))
    num2 = float(input("Give the second number: "))
    nsum = num1 + num2
    print("The sum of the numbers is: %f" % nsum)

def second():
    w = float(input("Give the width of the box: "))
    l = float(input("Give the length of the box: "))
    h = float(input("Give the height of the box: "))
    volume = w * l * h
    print("The volume of the box is: %s" % volume)

def third():
    year = date.today().year
    name = str(input("What is your name: "))
    birth = int(input("What is your year of birth: "))
    print("%s was born in %i and is %i years old in %i" % (name.capitalize(), birth, year - birth, year))

def fourth():
    passlen = int(input("What length should the password be: "))
    chars = printable[:-15]
    password =  "".join(sample(chars, passlen))
    print("Your generated password is: %s" % password)
