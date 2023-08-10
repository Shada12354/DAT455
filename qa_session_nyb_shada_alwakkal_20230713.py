"""
QA-session Beginner (Nyb) 2023-07-13
@author Shada Al-Wakkal, GitHub: Shada12354

Länk till https://pypi.org/project/graphics.py/#files,
John Zelles graphics.py package, for use with the textbook "Python Programming: An Introduction to Computer Science"
Länk till dokumentation: https://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf, https://mcsp.wartburg.edu/zelle/python/graphics.py
Obs: se till att filen finns i samma mapp som ditt Python Script.
"""

from graphics import *

#Skapa ett fönster
window = GraphWin("Hello Graphics", 400, 400)

#Rita en punkt
point = Point(250,250)
point.draw(window)

#Fyll i punkten
point.setFill("BLUE")

#Säg hej till användaren
txt = Text(Point(200,200), "Hello all!")
txt.setSize(20)
#txt.setStyle("bold")
txt.draw(window)

#Rita en rektangel
rectangle = Rectangle(Point(120,250), Point(240,300))
rectangle.draw(window)

#Rita en kvadrat
square  = Rectangle(Point(50,50), Point(100,100))
square.draw(window)

#Rita en triangle
p1 = Point(270,270)
p2 = Point(300,400)
p3 = Point(400,270)
triangle = Polygon(p1,p2,p3)
triangle.draw(window)

#Rita en cirkel
circle = Circle(Point(100,150),20)
circle.draw(window)
circle2 = Circle(Point(250,250),5)
circle2.draw(window)
circle2.setFill("GREEN")

#Window2
window2 = GraphWin("Hello Graphics 2", 200,400)
txt2 = Text(Point(-100,200), "Hello all!")
txt2.setSize(20)
#txt.setStyle("bold")
txt2.draw(window2)

#Window3
window3 = GraphWin("Purple window", 100, 100)
window3.setBackground("PURPLE")



#Stäng fönstret
window.getMouse()
window.close()

window2.getMouse()
window2.close()

window3.getMouse()
window3.close()
