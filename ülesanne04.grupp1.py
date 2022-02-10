################
# ülesanne 04  #
# Dajana Mähdi #
#  03.02.2022  #
################

#Ruutude ja kuupide tabel
number = 0
square = 0
cube = 0

for number in range(1,6):
    square = number * number
    cube = number * number * number
    print(number,square,cube)


#Pank
konto = 0
raha = 10000
intress = 0.05
aastad = 5
konto += raha
print(f"{'aasta':4} {'algsumma':10} {'intress':10} {'aasta lõpuks':10}")
for i in range(aastad):
    kasum = konto*intress
    print(f"{i+1+4} {konto:10.2f} {kasum:10.2f} {konto+kasum:10.2f}")
    konto+=kasum

#Arvamismäng
import random
nr = 12
loop = 1
kordade_arv = 0
 
print('Arva ära number 1-50')
 
while loop == 1:
    arva = int(input('Sisesta täisarv: '))
    
    if arva == nr:
        kordade_arv += 1
        print('Tubli, pakkumisi kokku: ',kordade_arv)
        loop = 0
    elif arva < nr:
        kordade_arv += 1
        print('Sinu pakutud arv on liiga väike')
    else:
        kordade_arv += 1
        print('Sinu pakutud arv on liiga suur')

#Viisikud
for i in range(1,101):
    if i%5==0:
        print(i)
   
#Pisike korrutustabel
for i in range(1,6):
    for j in range(1,6):
        print('{0:>3}'.format(j*i), end=" ")
    print()

#Paaris ja Paaritu
for i in range(1,101):
    if i%2==0:
        print(f"{i} paaris")
    else:
        print(f"{i} paaritu")

#Loto
from random import randrange
for i in range(1,6):
    print(randrange(0,9),end="")
print()
     
#Tärnid
for i in range(1,6):          
    for j in range(1,6):       
        print('* ', end='')
    print()
    
#Kasvav kolmnurk tärnidest
for i in range (1,6):
    print(i*"* ")
    
#Kahanev kolmnurk tärnidest
hoius = 6
for i in range (1,hoius+1):
    print(hoius*"* ")
    hoius = hoius-1
    
    
    
#Jalgpalli meeskond
sugu=input("sisestage oma sugu (soo esimene täht): ")
if sugu=="m":
    vanus=int(input("sisestage oma vanus: "))
    if vanus>=16 and vanus <=18:
        print("Sa oled meeskonnas! Mario kaasa mitte tuua :)")
    else:
        print ("sa ei sobi meie tiimi, mine ära ja ära tagasi tule:)")

else:
    print("Sa ei sobi kuna sa naine, mine ära :)")
    
     
#Müük
hind=int(input("Sisesta toote hind: "))
if hind <= 10:
    ale=0.1
else:
    ale=0.2
hind=hind-hind*ale
print("hind on",hind,"eurot")


#ruut
a = int(input("1. kylg: "))
b = int(input("2. kylg: "))
if a==b:
     print("Ruut")
else:
    print("Ristkülik")
   
#matemaatika
arv1= int(input("sisesta arv 1: "))
arv2=int(input("sisesta arv 2: "))
tehe=int(input("\n 1) liitmine\n 2) lahutamine\n 3) korrutamine\n 4) jagamine\nvali tehe: "))
if tehe==1:
    v=arv1 + arv2
elif tehe==2:
    v=arv1 - arv2
elif tehe==3:
    v=arv1 * arv2
else:
    v=arv1 / arv2
print(f"{arv1}{tehe}{arv2}={v}")

#Juubel
synd = input("Sisesta sünniaeg kujul pp.kk.aa: ")
p, k, a = synd.split(".")
vanus = 2022- int(a)
if vanus%5 == 0:
    print("on juubel")
else:
    print("Ei ole jubel")
    










