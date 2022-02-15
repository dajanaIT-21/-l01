##################
#       ü5       #
#  Dajana Mähdi  #
#   10.06.2022   #
##################

#Tärnid
arvud = [29,87,65,17,90]
for i in range(len(arvud)):
    print("*"*arvud[i])


#Vanused
import random
arvud = []
for i in range(5):
    arvud.append(random.randint(1,99))
print("suurim arv: ", max(arvud))
print("väikseim arv: ",min(arvud))
print("kokku: ",sum(arvud))
print("keskmine: ",sum(arvud)/len(arvud))


#Dublikaadid
nimed = ['juhan','juhan','mati','maaria','mati']
puh_nimed = []
#kontrollib kordust
for i in range(len(nimed)):
    if nimed[i] not in puh_nimed:
        puh_nimed.append(nimed[i])
#kuvas õpilased        
for i in range(len(puh_nimed)):
    print(puh_nimed[i],end=", ")

print()

#õpilased
opilased = ['juhan','kati','mati','maaria','mario']
print("vali nr mida soovid muuta: ")
for i in range(len(opilased)):
    print(f"{i+1}. {opilased[i]}")
valik = int(input("sisesta number: "))
del opilased[valik-1]
print(opilased)
uus_nimi = input("sisesta new v muudetud name: ")
opilased.insert(valik-1,uus_nimi)
print("nimi on sucessfuly muudetud")
print(opilased)


#Nimede lisamine loendisse
nimed = []
for i in range(5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)


    
