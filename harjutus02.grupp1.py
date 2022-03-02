import math
# Harjutus 2
# Dajana Mähdi
# 31.01.2022

#kolmnurga ümbermõõt
a,b,c = 1,2,3
p = a+b+c
print("kolmnurga ümbermõõt on:",p)

#toote hinna leidmine
hind= 36.75
ale= 0.4
kogus= 3
summa = (hind-(hind*ale))*3
print("kolme toote summa:",summa,"€")

#pitsa kolmele sõbrale
hind=12.90
protsent=0.1
inimesed=3
kokku=((hind*protsent)+hind)/inimesed
print("igaüks peab maksma:",kokku,"€")
              
#Rulluisutajate kiirus
kiirus=29.9
aeg=24
vahemaa=(kiirus*aeg)
print("rulluisutaja jõuab 24 minutiga:",vahemaa,"meetri kaugusele")

#Hüpotenuus
a,b = 1,2
c = math.sqrt(a**2+b**2)

#arvusüsteemid
arv = int(input("sisesta 10nd arv: "))
print(bin(arv))
print(hex(arv))

#ajateisendus
minutid = int(input("sisesta minutid: "))
tund = minutid//60    #täisarvuline jagamine
minut = minutid%60    #jäägi leidmine
print(minutid, "minutid on", tund,":", minut)

#kütusekulu arvutamine
liiter = 20
dist = 200
kulub = liiter/(dist/100)
print(kulub)




        
        
        
        
        
        
        
        
        
        
        
        
        
