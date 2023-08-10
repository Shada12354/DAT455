"""
QA-session Beginner (Nyb) 2023-07-04
@author Shada Al-Wakkal, GitHub: Shada12354
"""

class Hello_World:
    def __init__(self,name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}")
        print("I'm just a computer in this world, out to seek knowledge")

human = Hello_World("Shada")
human.hello()



from graphics import *

class Message:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw_message(self):
        window = GraphWin("Hello Graphics",400,400)
        txt = Text(Point(self.x,self.y),"Hello all")
        txt.setSize(20)
        txt.setStyle("bold")
        txt.draw(window)
        window.getMouse()
        window.close()

msg = Message(200,200)
msg.draw_message()



class Team:
    def __init__(self,team):
        self.team = team

    def best_team_in_the_world(self):
        if self.team == "Real Madrid":
            print("YES!")
        else:
            print("NO, REAL MADRID IS BEST")
            print("To argue, argue()")

    def argue(self):
        print("REAL, BEST TEAM IN THE WORLD!!!!")


team = input("What team is the best in the world > ")
answer = Team(team)
answer.best_team_in_the_world()
answer.argue()


class Greet:
    def speak(self):
        print("Hello World!")

hello = Greet()
hello.speak()

class Team:
    def __init__(self,team):
        self.team = team
    def best_team_in_the_world(self):
        if self.team == "Real Madrid":
            print("yes")
        else:
            print("no rm is best")
            print("to argue, argue()")
    def argue(self):
        print("real madrid is the best team")
team = input ("what team is the best team")

answer = Team(team)
answer.best_team_in_the_world()
answer.argue()


