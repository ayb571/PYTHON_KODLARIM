#PYTHON KODLAR


                                       #Girilen iki sayıdan ikincisinin birincisine bölümünü bulma  

# print("Cıkmak icin sıfıra basınız!!")
# cıkıs=1
# while cıkıs!=0:
#       cıkıs =int(input("Cıkmak icin sıfıra bas,devam etmek icin baska sayı girin:"))

#       if cıkıs==0:
#            print("Cıkıs yapılıyor.")
#       break 

#       num=int(input("Birinci sayiyi giriniz:"))
#       num2=int(input("İkinci sayiyi giriniz:"))

#       if num2==0:
#             print("İkinci sayı sıfır olamaz Sayı girin.")
#       else:
#             print("İkinci sayının birinci sayıya bolumu {}".format(num/num2))




                                    #Girilen iki sayıdan ikinciyi, birincinin üssü olarak yazma


# x=int(input("Birinci sayıyı giriniz:"))
# y=int(input("İkinci sayıyı giriniz:"))
# num=0
# sonuc=1
# while num<y:
#     sonuc*=x
#     num+=1
# print("{0} ussu {1}, {2} eder".format(x,y,sonuc))    




# notlar_toplamı=0

# for x in range(10):
#     notlar=int(input("{}.Notu giriniz=".format(x+1)))
#     notlar_toplamı+=notlar
# print("Notların toplamı=",notlar_toplamı)
# print("NOTLARIN ORTALAMASI={}".format(notlar_toplamı/10))








#Girilen bir kelimenin uzunluğunu kontrol et, 5 karakterden uzunsa "Uzun kelime" yazdır.

# kelime=input("Kelime giriniz:")

# kelime_uzunluk=len(kelime)
# if kelime_uzunluk>5:
#     print("Uzun kelime ")
# else:
#     print("Uzun degil")



#Kullanıcının girdiği yılın artık yıl olup olmadığını kontrol et.

# yıl=int(input("yıl girin:"))

# if (yıl%4==0 and yıl%100!=0) or yıl%400==0:
#     print("Artık yıldır")
# else:
#     print("artık yıl degildir")



                               
#Girilen bir harfin sesli harf olup olmadığını kontrol et.

# harf=input("harf giriniz=")
# if harf==["a", "e", "ı", "i"," o"," ö", "u", "ü" ]:
#     print("Harfiniz sesli harftir.")
# else:
#     print("Harfiniz sessiz harftir")



#Girilen bir karakterin rakam olup olmadığını kontrol eden program yaz.

# Karekter=input("Kareketer giriniz:")
# if Karekter.isdigit():
#     print("karekteriniz rakamdır.")
# else:
#     print("Rakam degildir")




                                       #Girilen üç sayıdan en büyüğünü bulan program yaz.
# x=int(input("Birinci sayıyı giriniz:"))
# y=int(input("ikinci sayıyı giriniz:"))
# z=int(input("ucuncu sayıyı giriniz:"))

# if x<y and z<y :
#     buyuk_sayı=y
# if x<z and y<z :
#     buyuk_sayı=z
# if y<x and z<x :
#     buyuk_sayı=x
# print("Buyuk sayınız:",buyuk_sayı)




#Girilen bir gün adının hafta içi mi hafta sonu mu olduğunu söyleyen program yaz.

# gun=input("Bir gün giriniz:").capitalize()
# print(gun)

# haftaici=["Pazartesi","Salı","Carsamba","Persembe","Cuma"]

# if gun in haftaici:
#     print("Girdiginiz gun haftaiçi")
# else:
#     print("Hafta sonu")


#Kullanıcının yaşına göre "Çocuk (0-12)", "Genç (13-19)", "Yetişkin (20+)" sınıflandırması yap.

# yas=int(input("Yas degerini girin:"))
# if  0<yas<12:
#     print("Cocuk katagorisindesiniz.")
# if  13<yas<19:
#     print("Genc katagorisindesiniz.")
# if  20<yas:
#     print("Yetiskin katagorisindesiniz.")
           








#DEMET
# gun=input("Turkce gun girin")
# tren={'pazartesi':'monday','salı':'truesday','carsamba':'wednesday'}
# print("ingilizcesi..:",end="")
# print(tren.get(gun))




                                                                 #CLASS VE METOTLAR
# class Araba:
#     def __init__(self,model,fiyat):
#         self.model=model
#         self.fiyat=fiyat 
#     def AracBilgisi(self):
#         print("model:",self.model)
#         print("fiyat:",self.fiyat)
#         print("Renk:",self.renk)
# class Kamyon(Araba):
#     def __init__(self, model, fiyat, renk):
#         Araba.__init__(self,model,fiyat)
#         self.renk=renk
 

# Taksi=Kamyon(2025,5000000,"gold")
# Taksi.AracBilgisi()