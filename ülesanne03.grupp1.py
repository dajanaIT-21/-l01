# harjutus 03
# Dajana Mähdi
# 01.02.2022

#Korralik nimi
nimi = input("sisesta nimi: ")
#nimi = nimi.capitalize()
nimi = nimi.strip().capitalize()
print("Tere",nimi+"!")

#vandumine
s = input("Ära kurat ütle: ")
s = s.lower()
v = s.replace("kurat","*****")
print(v)

#email
email = input("sisesta ome email: ")
print("@" in email)

#tundide ajad
aeg1 = input("alguseaeg: ")
aeg2 = input("lõpuaeg: ")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2))-(int(hh1)*60+int(mm1))
h = vastus//60
m = vastus%60
print(f"{h}:{m}")

#palindroom
sisestus = input("sisesta palindroom: ")
print(sisestus == sisestus[::-1])



