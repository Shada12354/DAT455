""""
QA-session Beginner (Nyb) 2023-06-29
@author Shada Al-Wakkal, GitHub: Shada12354
"""
import math
import random

#BINARY CONVERSION
print(bin(5))
print(int("101", 2))


#N CHOOSE K COMBINATIONS
def combination(n,k):
    c = math.factorial(n)/ (math.factorial(n-k)*math.factorial(k))
    return c
print(combination(5,2))

#PERCENTAGE
def percentCal(n,part,roundOff):
    percent = (part/n * 100)
    if roundOff == 0:
        percent = math.floor(percent)
        return percent
    elif roundOff == 1:
        percent = math.ceil(percent)
        return percent
    else:
        return percent

print("Enter numbers to calculate percentage>")
print("Enter demoniator>")
n = float(input())
print("Enter numerator")
p = float(input())
print("Round down(0), round upp(1), no round off (2)")
choice = float(input())
print(percentCal(n,p,choice))

#FIBONACCI SEQUENCE
def fib(n):
    a,b = 0,1
    while a < n:
        print(a)
        a,b = b, a+b
    print()

fib(100)


#COINFLIP

print("Welcome to my coin flipping game!")
choice = input("Enter your choice, heads or tails> ")

num = random.randint(1,2)

if num==1:
    result = "heads"
elif num==2:
    result = "tails"

if choice == result:
    print("Good job, the coin flipped ", result)

else:
    print("You loose, coin flipped ", result)

print("Thanks for playing!")


"""
binaryconv.py - from course Github
"""


import math

def bin2dec(bin):
    dec = 0
    for b in range(len(bin)):
        dec = dec + (2 ** (len(bin) - b - 1)) * int(bin[b])
    return dec, bin

print(bin2dec("10000"))
print(bin2dec("01010"))

def dec2bin(dec):
    bin = ""
    while dec > 0:
        bit = str(dec % 2)
        bin = bit + bin
        dec = dec // 2
    return bin, dec

print(dec2bin(3))
print(dec2bin(2))
def binTable(dec):
    for n in range(1, dec + 1):
        bn = dec2bin(n)[0]
        print(n, "\t", bn)

binTable(10)
binTable(4)

def testDecBin(dec):
    bin = dec2bin(dec)[0]
    bdec = bin2dec(bin)[0]
    if bdec == dec:
        print(dec, bin, "OK")
    else:
        print(dec, bin, bdec, "ERROR")

testDecBin(10)
testDecBin(4)


def sum(n):
    s = 0
    for k in range(1, n + 1):
        s = s + k
    return s, n

print(sum(6))
print(sum(12))


def factorial(n):
    fac = 1
    for k in range(2, n + 1):
        fac = fac * k
    return fac, n

print(factorial(2))
print(factorial(5))


def precisionLoss(n, iters):
    c = n
    for i in range(iters):
        r = c / 3
        c = 3 * r
        print(c)

precisionLoss(4, 4)
precisionLoss(1, 9)


def swedish(d):
    return int(d + 0.5), d

print(swedish(5.9))
print(swedish(0.00301))


def approxPi(n):
    div = 1
    sign = 1
    pi = 0
    for k in range(n):
        pi = pi + 4 / div
        sign = - sign
        div = sign * (abs(div) + 2)
    return pi, n

print(approxPi(10))
print(approxPi(2))


def quadraticEq(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr < 0:
        return [], (a, b, c)
    elif discr == 0:
        return [-b / (2 * a)], (a, b, c)
    else:
        rdiscr = math.sqrt(discr)
        return [(-b - rdiscr) / (2 * a), (-b + rdiscr) / (2 * a)], (a, b, c)

print(quadraticEq(1, 5, 5))
print(quadraticEq(-1, 5, -1))

def multiTable(n):
    for x in range(1, n + 1):
        row = ""
        for y in range(1, n + 1):
            row = row + "\t" + str(x * y)
        print(row)

multiTable(5)
def hypotenuse(a, b):
    return math.sqrt(a * a + b * b), (a, b)

print(hypotenuse(5, 9))
print(hypotenuse(-5, 9))
def pythagoreans(mx):
    for c in range(mx):
        for b in range(1, c):
            for a in range(1, b):
                if a * a + b * b == c * c:
                    print(a, b, c, ":", a * a, "+", b * b, "=", c * c)

pythagoreans(17)
pythagoreans(8)


def newton(r, n):
    guess = r / 2
    for i in range(n):
        guess = (guess + r / guess) / 2
        print(guess, "\terror:\t", math.sqrt(r) - guess)
    return guess, (r, n)

print(newton(4, 9))
print(newton(1, 3))
