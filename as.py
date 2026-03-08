# PYTHON EGİTİMİM...(BTK)

#import keyword
#keyword.kwlist

#yas=(input('yasınız:'))
#print('yasınız:',yas)

#print('b ',' t ',' k',sep='+')                SEP KULLANIMI

#print("yasınız ?", end=(':'))
#yas=input('Yasınız:')
#print("yasınız:",yas)


   # A=10
   # print("A={0}".format(A))

#A=15
#print(f"a={A}")

#print("1.sınav",end=(':'))                     YAŞ BULMA OYUNU
#sınav1=int(input())
#print("2.sınav",end=(':'))
#sınav2=int(input())
#ort=0
#ort=(sınav1+sınav2)/2
#print("ortalamanız:",ort)

#dt=int(input("Dogum tarihinizi giriniz:"))
#yas=2025-dt
#print("Yasınız:",yas)

#a=int(input("Bir sayı giriniz:"))               SAYI TAHMİN OYUNU
#b=int(input("Girilen sayıyı tahmin et:"))
#if a==b:
#    print("Tahmin dogru")
#else:
#    print("Tahmın yanlış")


#num=int(input("Bir sayı giriniz:"))              tek ve çift sayı bulma
#if num%2==0 :
#    print("Sayınız çift sayıdır.")
#else:
#    print("Sayınız tek sayıdır.")



#Liste=[1,2,3,4,5]                                 LİSTE YONTEMİ
#print(Liste)


#liste=[1,2,3,4,5,6,9]                             APPEND KOMUTU
#print(liste)
#liste.append(10)
#print(liste)



#X=1                                              WHİLE DONGUSU İLE KARE ALMA İŞLEMİ
#print("Cikis icin sıfıra basınız")
#while(X!=0):
# X=int(input("Sayı girin:"))
 #print("Sayının karesi:",X*X)
#print("Gule gule")



#print("Cıkmak icin 0 a basın.")              While true ile sonsuz dongu
#while True:
    #X=int(input("Bir sayı girin:"))
    #print("Karesi:",X*X)
    #if(X==0):
     #break #Dönguden cık





#for A in range(100):
     #if(A%7==0):
         #continue
     #print(A)



#for A in range (1,11):
    #for B in range(1,11):
        #print(A,"*",B,"=",A*B)
    #print("\n")



#def selamlama(isim):                                               FONKSİYON
   # print("Sayın",isim,"restaurantımıza hos geldiniz")

#while True:
    #isim=input("İsminiz nedir?")
    #selamlama(isim)




#def alan(u,k):                              Dikdortgenin Alan ve cevresi
#    A=u*k
#    return A
#def cevre(u,k):
#    B=2*(u+k)
#    return B
#u=int(input("uzun kenarı giriniz:"))
#k=int(input("kısa kenarı giriniz:"))
#print("Alan:",alan(u,k))
#print("Cevre:",cevre(u,k))




            

 
                                              ##Girilen iki sayıdan küçük olanı bulma


#num=int(input("Birinci sayıyı giriniz:"))
#num2=int(input("İkinci sayıyı giriniz:"))
#if num>num2:
    #print(f"{num} sayısı {num2} sayısından buyuktur")
#else:
    #print(f"{num2} sayısı {num} sayısından buyuktur")




                                                     #Girilen üç sayıdan en büyük olanı bulma

#num=int(input("Birinci sayıyı giriniz:"))
#num2=int(input("İkinci sayıyı giriniz:"))
#num3=int(input("ucuncu sayıyı giriniz:"))
#if num>num2 and num>num3:
#    en_buyuk=num
#elif num2>num and num2>num3:
#    en_buyuk=num2
#else: 
#    en_buyuk=num3

#print(f"En buyuk sayınız:{en_buyuk}")






# num=0
# yazarlar=["Oguz Atay","Orhan Pamuk","Peyami Safa","Sabahattin Ali","Ahmet Hamdi Tanpınar"]
# for yazar in yazarlar:
#     num+=1
    
#     ad,soyad=yazar.split()[0],yazar.split()[1]
#     print("{0} => Adı {1} ve Soyadı {2}".format(num,ad,soyad))
    








