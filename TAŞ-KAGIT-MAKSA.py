import random
Liste=["Tas","Kagıt","Makas"]
PC=random.choice(Liste)
oyuncu=input("Tas,Kagıt,Makas ucunden biriniz yazınız=").capitalize()
print("Oyuncu seçimi={}".format(oyuncu))
print("PC seçimi={}".format(PC))
if PC==oyuncu:
    print("Berabere kaldınız...")
if (PC=='Tas') and (oyuncu=='Kagıt'):
     print("Oyuncu kazandı...")
if (PC=='Tas') and (oyuncu=='Makas'):
     print("PC kazandı...")
if (PC=='Kagıt') and (oyuncu=='Tas'):
     print("PC kazandı...")
if (PC=='Kagıt') and (oyuncu=='Makas'):
     print("Oyuncu kazandı...")
if (PC=='Makas') and (oyuncu=='Tas'):
     print("Oyuncu kazandı...")
if (PC=='Makas') and (oyuncu=='Kagıt'):
     print("PC kazandı...")



