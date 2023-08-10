""""
QA-session Beginner (Nyb) 2023-07-11
@author Shada Al-Wakkal, GitHub: Shada12354
"""

try:
    date = int(input("Enter your birthday, yymmdd fromat >>"))
except ValueError:
    print("Invalid format")
except:
    print("The program is running nicely")
finally:
    print("This program is for your birthday")

"""
Rest of code is from  Python Programming: An Introduction to Computer Scienc - John Zelle
"""
def is_integer(num):
    return isinstance(num, int)


print("Enter three numbers please, enter after each")
a = int(input())
b = int(input())
c = int(input())

while (is_integer(a) != True) and (is_integer(b) != True) and (is_integer(c) != True):
    print("That is not an int, please enter an int. Use enter after each")
    a = int(input())
    b = int(input())
    c = int(input())

if a > b:
    if b > c:
        print("Spam Please!")
    else:
        print("It's a late parrot!")
elif b > c:
    print("Cheese shoppe")
    if a >= c:
        print("Cheddar")
    elif a < b:
        print("Gouda")
    elif c == b:
        print("Swiss")

else:
    print("Trees")
    if a == b:
        print("Chestnut")
    else:
        print("Larch")

print("Done")



#7. The Boolean operator or returns True when both of its operands are true.
x,y = 10,15
z,w = 20,25
print(x < y or z < w)

#8. a and (b or c) == (a and b) or (a and c)
a = x < y #true
b = w < z #false
c = z > w #false
print(a and (b or c) == (a and b) or (a and c))

#9. not(a or b) == (not a) or not(b)
print( (not (a or b) ) == ( (not a) or (not b) ) )

"""
datediff, modified - from course Github,modified by me.
"""


from datetime import datetime, timedelta
def yearLength(year):
    if year % 400 == 0:
        return 366
    elif year % 100 == 0:
        return 365
    elif year % 4 == 0:
        return 366
    else:
        return 365

def monthLength(year,month):
    if month == 2 and yearLength(year) == 366:
        return 29
    elif month == 2:
        return 28
    elif month in [4,6,9,11]:
        return 30
    else:
        return 31

def dateDays(year,month,day):
    days = 0
    for y in range(year):
        days = days + yearLength(y)
    for m in range(1,month):
        days = days + monthLength(year,m)
    return days + day

def dateDiff(year1,month1,day1,year2,month2,day2):
    diff = dateDays(year2,month2,day2) - dateDays(year1,month1,day1)
    return diff


def checkDate(year,month,day):
    return (0 < month <= 12) and (0 < day <= monthLength(year,month))


def dateInput(prompt):
    date = input(prompt + ", format YYYY-MM-DD or MM/DD/YYYY > ")
    try:
        if '/' in date:
            month, day, year = map(int, date.split('/'))
        else:
            year, month, day = map(int, date.split('-'))

        if checkDate(year, month, day):
            return year, month, day
        else:
            print("Invalid format")
            return dateInput(prompt)

    except ValueError:
        print("Invalid format. Please enter YYYY-MM-DD or MM/DD/YYYY > ")
        return dateInput(prompt)

def RelativeDate(prompt):
    date = input(prompt + " 'today' or 'tomorrow' > ")
    today = datetime.now().date()

    if date == 'today':
        return today.year, today.month, today.day
    elif date == 'tomorrow':
        tomorrow = today + timedelta(days=1)
        return tomorrow.year, tomorrow.month, tomorrow.day
    else:
        print("Invalid date. Enter 'today' or 'tomorrow'. > ")
        return RelativeDate(prompt)


def main():
    try:
        while True:
            choice = input(" 'R' for relative date, 'D' for specific date, or 'Q' to quit > ")
            if choice.upper() == 'Q':
                break
            elif choice.upper() == 'R':
                try:
                    year1, month1, day1 = RelativeDate(" Relative start date >")
                    year2, month2, day2 = RelativeDate(" Relative end date >")
                    print("Difference is", dateDiff(year1, month1, day1, year2, month2, day2))
                except Exception as e:
                    print("An error occurred:", e)
            else:
                try:
                    year1, month1, day1 = dateInput("Start date >")
                    year2, month2, day2 = dateInput("End date >")
                    print("Difference is", dateDiff(year1, month1, day1, year2, month2, day2))
                except Exception as e:
                    print("An error occurred:", e)

    except KeyboardInterrupt:
        print()
        exit_choice = input("Exit? 'Q' > ")
        if exit_choice.upper() == 'Q':
            print("Goodbye!")
        else:
            main()
    except:
        print()
        print("Okay, goodbye")


if __name__ == '__main__':
    main()
