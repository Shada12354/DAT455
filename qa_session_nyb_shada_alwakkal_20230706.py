""""
QA-session Beginner (Nyb) 2023-07-06
@author Shada Al-Wakkal, GitHub: Shada12354
"""
import math

txt1 = "Hello World, what a wonderful day"
copytxt1 = txt1.split()
print(copytxt1)
copytext1_2 = txt1.split(",")
print(copytext1_2)

txt2 ="#Apple#Photo#food#cars"
copytxt2 = txt2.split("#")
print(copytxt2)
copytxt2_2 = txt2.split("#",1)
print(copytxt2_2)

txt3 ="               Apple            "
print(txt3)
txt3 = txt3.split()
print(txt3)

txt4 = ",,,axg,,,, Mango ,,,,,hjy"
print(txt4)
txt4 = txt4.strip(",axghjy")
print(txt4)

num = [9,8, 9, 10, 200, 25]
print(sorted(num))
num.sort()
print(num)

f = lambda x: math.cos(x)**2 + math.sin(x)**2
print(f(0.3))

Z = lambda x,y: math.cos(x)**2 + math.sin(y)**2
print(Z(0.7, 0.9))

print(sorted(num, key= lambda x:-x))
print(sorted(num,reverse=True))

"""
from  Python Programming: An Introduction to Computer Scienc - John Zelle
"""

def getNum():
    nums = []

    xlist = input("Enter a number >>")
    while xlist != " ":
        x = eval(xlist)
        nums.append(x)
        xlist = input("Enter a number >>")
        return nums

def mean (nums):
        sum = 0.0
        for num in nums:
            sum = sum + num
        return  sum/len(nums)


print(mean(getNum()))
"""
dict_lookup - from course GitHub
"""
import sys

def mkDict(lines,src,tgt):
    dict = {}
    for line in lines:
        fields = line.split(';')
        if len(fields) >= 2:
            for word in fields[src].split(','):
                sword = word.strip()
                dict[sword] = dict.get(sword,[])
                for trans in fields[tgt].split(','):
                    dict[sword].append(trans.strip())
        elif fields:
            pass # print("INTE MED", line)
        else:
            pass
    return dict

def readDict(filename,src,tgt):
    file = open(filename)
    lines = file.readlines()
    file.close()
    return mkDict(lines,src,tgt)


def main():

    if len(sys.argv) > 2:
        filename = sys.argv[1]
        src,tgt = sys.argv[2].split(',')
        dict = readDict(filename,int(src),int(tgt))
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        dict = readDict(filename,0,1)
    else:
        print("dictionary lookup from ;-separated files")
        print("usage: dict_lookup <dictfile.csv> <from_column,to_column>?")
        return
    prompt = "ange sökord+enter, sluta med enter> "
    query = input(prompt)
    while query:
        for trans in dict.get(query,["hittar inte"]):
            print(trans)
        query = input(prompt)

if __name__ == "__main__":
    main()


##############

# make a lemmatization lexicon produced from lists lemma,form,...form

def mkLemmaDict(lines):
    dict = {}
    for line in lines:
        words = line.split(',')
        lemma = words[0].strip()
        for word in words[1:]:
            sword = word.strip()
            if sword not in dict:
                dict[sword] = [lemma]
            elif lemma not in dict[sword]:
                dict[sword].append(lemma)
            else:
                pass
    return dict
