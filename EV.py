from turtle import*
colormode(255)
color(0,0,0)
pensize(5)
def ucgen():
    for x in range(3):
        fd(150)
        left(120)  
def kare():
    for x in range(4):
        fd(150)
        rt(90)

begin_fill()
fillcolor("brown")
ucgen()
end_fill()

begin_fill()
fillcolor("yellow")
kare()
end_fill()