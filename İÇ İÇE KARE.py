from turtle import*
def karecizimi(mesafe):
    for a in range(1,5):# Bir Karenin yapılışı
        fd(mesafe)
        rt(90)


pensize(1) # KALINLIGI AYARLAMADA KULLANILIR
x=int(input("Kare sayısını giriniz:"))
for a in range(x):
    karecizimi(50*a)