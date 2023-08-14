""""
QA-session Beginner + Advanced (Nyb + Adv) 2023-08-10
@author Shada Al-Wakkal, GitHub: Shada12354

These answers are my own.
Good luck on the exam!
"""

"""
Exam: exam-january-2021
"""



#Question1
def legal_status(age):
    if age < 18:
        return 'minor'
    elif age >= 18 and age < 21:
        return 'adult'
    elif age >= 21 and age < 30:
        return 'alcohol'
    elif age >= 30 and age < 35:
        return 'senator'
    else:
        return 'president'

def main():
    age = int(input("What is your age? >"))
    status = legal_status(age)
    print(f"Your legal status is: {status}")

if __name__ == '__main__':
    main()

"""
#Question2
"""
def duplicate(xs):
    dict = {}
    result = []

    for x in xs:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1

    for x, count in dict.items():
        if count > 1:
            result.append(x)

    return result

#May not be needed for the exam, look in previous key/ask examiner.
print(duplicate([1,2,3,2,1,1,5]))
print(duplicate(['a','b','b','a']))
print(duplicate([True, False]))
print(duplicate([]))

"""
#Question3
"""
class DoorLock:
    def __init__(self, pin):
        self._pin = pin
        self._is_open = True

    @property
    def is_open(self):
        return self._is_open

    def lock(self):
        if self._is_open:
            self._is_open = False
            return True
        return False

    def unlock(self, pin_attempt):
        if not self._is_open and pin_attempt == self._pin:
            self._is_open = True
            return True
        return False

    def set_pin(self, pin_attempt, new_pin):
        if self._is_open and pin_attempt == self._pin:
            self._pin = new_pin
            return True
        return False

def main():
    pin = "1234"
    door_lock = DoorLock(pin)

    print("Initial state:", "Open" if door_lock.is_open else "Closed")
    print("Locking", door_lock.lock())
    print("State after locking", "Open" if door_lock.is_open else "Closed")

    unlock_attempt = input("Enter pin to unlock > ")
    if door_lock.unlock(unlock_attempt):
        print("Unlock successful, Door is open")
    else:
        print("Unlock failed, Door is closed")

    new_pin = input("Enter current Pin to set a new Pin >")
    new_pin_attempt = input("Enter new pin")
    if door_lock.set_pin(new_pin, new_pin_attempt):
        print("Pin changed successfully")
    else:
        print("Failed to change PIN")

    print("Final state ", "Open" if door_lock.is_open else "Closed")

if __name__ == "__main__":
    main()

"""
Exam: python-exam-220824
"""

def dat455():
    labs = input("Vilka labbar har du gjort? ").replace(" ", "").split(",")

    if "1" in labs and "2" in labs and "3" in labs:
        exam_score = int(input("Hur många poäng fick du i tentan? "))
        if exam_score >= 15:
            print("Grattis, du har klarat kursen!")
        else:
            print("Du har inte klarat kursen ännu, men du kan komma till omtentan.")
    else:
        print("Tyvärr kan du inte klara kursen den här gången.")

dat455()

