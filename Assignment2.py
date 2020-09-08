from datetime import date
from random import sample
from string import printable

def first():
    x = float(input("Give the first number: "))
    y = float(input("Give the second number: "))
    s = x + y
    print("The sum of the numbers is: %f" % s)

def second():
    w = float(input("Give the width of the box: "))
    l = float(input("Give the length of the box: "))
    h = float(input("Give the height of the box: "))
    v = w * l * h
    print("The volume of the box is: %s" % v)

def third():
    y = date.today().year
    n = str(input("What is your name: "))
    b = int(input("What is your year of birth: "))
    print("%s was born in %i and is %i years old in %i" % (n.capitalize(), b, y - b, y))

def fourth():
    l = int(input("What length should the password be: "))
    a = printable[:-15]
    p =  "".join(sample(a, l))
    print("Your generated password is: %s" % p)
