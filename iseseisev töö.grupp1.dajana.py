#on vaja luua suvalisi numbreid et täringu mängu mängida
import random

Mängia1_score = 0
pc_score = 0

# Korda kõike selles plokis 10 korda
for i in range(10):

    # Genereeri suvaline number mängijate jaoks
    Mängia1_value = random.randint(1, 6)
    pc_value = random.randint(1, 6)

    # Kuva väärtused
    Mängia1_pakkumine = random.randint(1, 101)
    print("Mängia 1 viskas: ", Mängia1_value)
    
    print("Arvuti viskas: ", pc_value)

    # väärtuste võrdluse põhjal vali sobiv tee läbi koodi.
    if Mängia1_value > pc_value:
        print("Mängia 1 võidab.")
        print("Mängia 1 võidab kogu laual oleva raha:)")
        Mängia1_score = Mängia1_score * 2  # Nii suurendame muutujat
    elif pc_value > Mängia1_value:
        print("Arvuti võidab")
        print("Arvuti võidab kogu laual oleva raha:)")
        pc_score = pc_score * 2
    
    else:
        print("Sen viik")

    input("Vajuta et jätkata.")  # Jätkamiseks oodake, kuni kasutaja sisestab.

print("### Mäng läbi ###")
print("Mängia 1 score:", Mängia1_score)
print("Arvuti:", pc_score)