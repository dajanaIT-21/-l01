###########################
#       ülesanne07        #
#      Dajana Mähdi       #
#       15.02.2022        #
###########################

#mata
import math
def kuup(a):
    v = a**3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3)
    return v

def konus(c):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(b):
    v = round(math.pi*r**2*h,2)
    return v

loop = 1

print("**************Leiame ruumala****************")
print("vali kujund:\n1 kuup\n2 kera\n3 koonus\n4 silinder\n5 EXIT")
valik = int(input("vali soovitud kujundi number: "))

if valik == 1:
    print("---------------------\nvalisid KUUBI ruumala arvutamise")
    a = int(input("sisesta kuubi külje pikkus a="))
    print(kuup(a))

if valik == 2:
    print("---------------------\nvalisid KERA ruumala arvutamise")
    r = int(input("sisesta kera raadiuse pikkus b="))
    print(kera(r))

if valik == 3:
    print("---------------------\nvalisid KOONUSE ruumala arvutamise")
    c = int(input("sisesta koonuse külje pikkus a="))
    print(konus(c))

if valik == 4:
    print("---------------------\nvalisid SILINDRI ruumala arvutamise")
    b = int(input("sisesta silindri külje pikkus a="))
    print(silinder(b))

#funktsioon
#loob funktsiooni atribuutidega
def tervita(nimi, keel="de"):
    if keel=="et":
        print(f"jou {nimi}!")
    elif keel=="en":
        print(f"hi {nimi}!")
    else:
        print(f"hallo {nimi}!")
    
n = input("sisesta nimi: ")
k = input("vali keel et/en/de: ")
#funktsiooni väljakustsumine
tervita(n,k)

