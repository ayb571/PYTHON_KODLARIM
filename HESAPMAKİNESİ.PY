import math                                        
while True:
    print("\n")
    print("NOT='Cıkmak için sıfıra basınız'")
    print("Toplama=1","Çıkarma=2","Bolme=3","Çarpma=4","Üssunu alma=5","Kökunu alma=6","Alan=7","Çevre=8",sep="\n")
    islem=int(input("0-8 ile dort arasında islem yapmak istediginiz rakami saciniz lutfen="))   
    if islem==0:
        print("Çıkış yapılıyor...")
        break
    if islem<0:
        print("Lutfen pozitif sayı giriniz !!!")
        continue  
    num1=int(input("Birinci sayiyi giriniz="))
    num2=int(input("İkinci sayiyi giriniz:"))  
    if num1<0 and num2<0:
        print("LÜTFEN POZİTİF TAM SAYI GİRİN !!!")
        continue
    if islem==1:
        Toplama=num1+num2
        print("Sayılarınızın toplamı={}".format(Toplama)) 
    if islem==2:
        if num1<num2:
            Cıkarma=num2-num1
            print("Sayılarınızın farkı={}".format(Cıkarma))
        else:
            Cıkarma=num1-num2
            print("Sayılarınızın farkı={}".format(Cıkarma))   
    if islem==3:
        if num1<num2:
            Bolme=num2//num1          
            print("Kucuk sayının buyuk sayıya bolumu={}".format(Bolme))
        else:
            Bolme=num1//num2
            print("Kucuk sayının buyuk sayıya bolumu={}".format(Bolme))
    if islem==4:
        Carpma=num1*num2
        print("Sayılarınızın carpımı={}".format(Carpma))
    if islem==5:
        gecici=1
        for i in range(1,num2+1):
            gecici*=num1 
        print("Birinci sayı taban ikinci sayı uss={}".format(gecici))   
    if islem==6:
        Kok=math.sqrt(num1)
        print("Birinci sayının koku={}".format(Kok))
        Kok2=math.sqrt(num2)
        print("İkinci sayının koku={}".format(Kok2))
    if islem==7:
        Alan=num1*num2
        print("Alanınız={}m²".format(Alan))
    if islem==8:
        Cevre=(num1+num2)
        print("Cevresi={} m".format(Cevre))
    
   


