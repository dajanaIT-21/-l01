#Täringud
#kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
#kasutaja võistleb kahe täringuga arvuti vastu - 1p
#kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
#kood kommenteeritud - 1p
import random

# Täringu mäng
Mängija1_punktid = 0
pc_punktid = 0
pank = 1000

# Korda kõike selles blokkis 10 korda
for i in range(10):

    # Looge iga mängija jaoks juhuslikud numbrid vahemikus 1 kuni 6.
    Mängija1_vaartus = random.randint(1, 6)
    pc_vaartus = random.randint(1, 6)

while pank > 0:
    print(f"Sul on {pank}$ panga kontol.")
    panus = int(input("Sisesta oma panus: "))

    # Kuva väärtused
    Mängija1_pakkumine = random.randint(1, 101)
    pc_pakkumine = random.randint(1, 101)
    print("Mängija 1 viskas: ", Mängija1_vaartus)
    print("Arvuti viskas: ", pc_vaartus)
    
    # väärtuste võrdluse põhjal vali sobiv tee läbi koodi
    if Mängija1_vaartus > pc_vaartus:
        print("Mängija 1 võidab.")
        print("Mängija 1 saab laual oleva raha:)")
        pank = pank + panus
        print(f"Sul on nüüd {pank}$ pangakontol")
        Mängija1_punktid = Mängija1_punktid 
        
    elif pc_vaartus > Mängija1_vaartus:
        print("Arvuti võidab")
        print("Arvuti saab laual oleva raha:)")
        pank = pank - panus
        print(f"Sul on nüüd {pank}$ pangakontol")
        Mängija1_punktid = Mängija1_vaartus
        pc_punktid = pc_vaartus
   
    else:
        print("Sen viik")

    input("Vajuta enter et jätkata.")
print()
print("### Mäng läbi ###")
print("Mängija 1 punktid:", Mängija1_punktid)
print("Arvuti punktid:", pc_punktid)