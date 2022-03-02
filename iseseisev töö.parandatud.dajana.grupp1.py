#TĆ¤ringud
#kuvatakse korrektne arusaadav kĆ¼simus ja hiljem vastus - 1p
#kasutaja vĆµistleb kahe tĆ¤ringuga arvuti vastu - 1p
#kasutaja teeb pakkumise ning suurima tĆ¤ringupunktisumma vĆµitja saab laual oleva raha endale - 2p
#kood kommenteeritud - 1p

import random

#Täringu mäng
Mängia1_score = 0
pc_score = 0
pank = 1000

# Korda kõike selles blokkis 10 korda
for i in range(10):

    # Looge iga mängija jaoks juhuslikud numbrid vahemikus 1 kuni 6.
    Mängia1_value = random.randint(1, 6)
    pc_value = random.randint(1, 6)

def total_bank(pank):
    pank = 1000
while pank > 0:
    print(f"Sul on ${pank} su panga kontol.")
    bet = int(input("Sisesta oma panus: "))


    # Kuva väärtused
    Mängia1_pakkumine = random.randint(1, 101)
    print("Mängia 1 viskas: ", Mängia1_value)
    
    print("Arvuti viskas: ", pc_value)
    
   
    # väärtuste võrdluse põhjal vali sobiv tee läbi koodi
    if Mängia1_value > pc_value:
        print("Mängia 1 võidab.")
        print("Mängia 1 võidab kogu laual oleva raha:)")
        pank = pank + bet
        print(f"Sul on nüüd ${pank} pangakontol")
        Mängia1_score = Mängia1_score +1  # Nii suurendame muutujat
    elif pc_value > Mängia1_value:
        print("Arvuti võidab")
        print("Arvuti võidab kogu laual oleva raha:)")
        pank = pank - bet
        print(f"Sul on nüüd ${pank} pangakontol")
        pc_score = pc_score +1
    
    else:
        print("Sen viik")

    input("Vajuta et jätkata.")  # Jätkamiseks oodake, kuni kasutaja sisestab.

print("### Mäng läbi ###")
print("Mängia 1 score:", Mängia1_score)
print("Arvuti:", pc_score)
