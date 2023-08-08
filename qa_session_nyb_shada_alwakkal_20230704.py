"""
QA-session Beginner (Nyb) 2023-07-04
@author Shada Al-Wakkal, GitHub: Shada12354
"""

def python_is_fun(x):
    python1 = "yes"


    txt = "Yes, Python is fun!"
    txt2 = "You are wrong, Python is fun!"

    if x == "yes":
        return txt
    else:
        return txt2

print("Do you like Python?")
x = input()
print(python_is_fun(x))

string1 = "10 8 9 1 19"
x = string1.isascii()
print(x)

string2 = "Välkommen till QA passet"
y = string2.encode()
print(y)

string3 = "hello world"
print(string3.endswith("!"))

string4 = "jag anvÄnder PyThon"
print(string4.capitalize())

string5 = "Det regnar ute, jag gillar regn"
print(string5.split(","))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
print(txt2)
txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt3)

fruits = ['äpple', 'bannan', 'apelsin']
fruits.clear()
print(fruits)

colors = ['Yellow', 'Purple', 'Pink']
c = colors.copy()
print(c)
print(colors)

cars = ['Volvo', 'Kia', 'BMW', 'BMW']
q = cars.count("BMW")
print(q)

computers = ['Apple', 'Lenovo', 'Asus']
computers.pop(0)
print(computers)

tv = ['samsung', 'LG', 'Sony']
tv.sort(reverse=True)
print(tv)

txt123 = "JAG VILL VISA OMVANDLING"
v = txt123.lower()
txt123 = txt123.lower()
print(v)
print(txt123)


"""
inivisble_ink.py - from course Github
"""
#Notera att programmet kan endast köras från terminalen!

import sys
import binaryconv as bc

def padbin(bin,n):
    need = 8 - len(bin)
    bin = need*'0' + bin
    return bin

def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(padbin(bc.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2txt(bin):
    txt = []
    while bin:
        txt.append(chr(bc.bin2dec(bin[:8])))
        bin = bin[8:]
    return "".join(txt)

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('\t')
    return "".join(inv)

def invisible2bin(inv):
    bin = []
    for b in inv:
        if b==' ':
            bin.append('0')
        elif b=='\t':
            bin.append('1')
        else:
            pass
    return "".join(bin)

#Orginal
def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))

""""
def txt2invisible(txt, separator):
    bin = txt2bin(txt)
    return bin2invisible(bin, separator)
"""

#Orginal
def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))

"""
def invisible2txt(inv):
    bin = invisble2bin(inv, separator)
    return bin2txt(bin)
"""
def main():
    mode = sys.argv[1]
    filename = sys.argv[2]
    file = open(filename)
    content = file.read()
    if mode == "develop":
        print(invisible2txt(content))
    else:
        print(txt2invisible(content))
    file.close()

main()

def simpleAsciiTable():
    for a in range(0,32):
        row = ""
        for k in range(0,8):
            row = row + str(a+32*k) + ' ' + chr(a+32*k) + '\t'
        print(row)


#Testa programmet
test_txt = input("Enter the name of file containing you wish to decode > ")
with open(test_txt, 'r') as file:
    txt_decode = file.read()
    invisble2txt_output = invisible2txt(txt_decode)
    print("Text decoded:", invisble2txt_output)

test_txt2 = input("Enter the name of file you wish to make invisble > ")
with open(test_txt2, 'r') as file:
    txt_invisible = file.read()
    txt2invisible_output = txt2invisible(txt_invisible)
    print("Text made invisble:", txt2invisible_output)
