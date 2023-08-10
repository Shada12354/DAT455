
""""
QA-session Beginner (Nyb) 2023-07-20
@author Shada Al-Wakkal, GitHub: Shada12354

"""
#Polymorphism
class Team:
    def is_best(self):
        pass

class Real_Madrid(Team):
    def is_best(self):
        return "Yes"

class Barcelona(Team):
    def is_best(self):
        return "No"

team1 = Real_Madrid()
team2 = Barcelona()

print(Real_Madrid.is_best(team1))
print(Barcelona.is_best(team2))

#Arv + Polymorphism
class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}")

    def ask(self):
        pass

class Person(Human):
    def __init__(self,name,nickname):
        super().__init__(name)
        self.nickname = nickname

    def speak(self):
        print(f"Or should I say {self.nickname}")

person = Person("Tintin", "Tin")
person.greet()

#Arv + Overriding

class Calc:
    def __init__(self,operation,operator1,operator2):
        self.operation = operation
        self.operator1 = operator1
        self.operator2 = operator2

    def addition(self):
        return self.operator1 + self.operator2

    def subtraction(self):
        return self.operator1 - self.operator2

    def multiplication(self):
        return self.operator1 * self.operator2


class MiniCalc(Calc):
    def __init__(self, operation, operator1, operator2):
        super().__init__(operation,operator1,operator2)

    def perform_operation(self):
        if self.operation == 1:
            return self.addition()

        elif self.operation == 2:
            return self.subtraction()

        else:
            return self.multiplication()

class MiniCalcV2(Calc):
    def __init__(self, operation, operator1, operator2, operator3):
        super().__init__(operation, operator1, operator2)
        self.operator3 = operator3

    def addition(self):
        return self.operator1 + self.operator2 + self.operator3

    def subtraction(self):
        return self.operator1 - self.operator2 + self.operator3

    def multiplication(self):
        return self.operator1 * self.operator2 * self.operator3

    def perform_operation(self):
        if self.operation == 1:
            return self.addition()

        elif self.operation == 2:
            return self.subtraction()

        else:
            return self.multiplication()

mini_calc = MiniCalc(1,2,19) #21
mini_calc_v2 = MiniCalcV2(3,4,2,3) #24
print(mini_calc.perform_operation())
print(mini_calc_v2.perform_operation())
