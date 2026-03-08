from turtle import*
N=int(input("Kenar sayısını giriniz:"))
aci=360/N
pensize(4)
for i in range(N):
    fd(100)
    rt(aci)
