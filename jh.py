import random
import time
#MENÜÜ TAOLINE ASI

print("          Valge Daam")
print(" Mängu tegid kaks saamatut inimest")
print("Dajana Mähdi ja Remy Rasmus Koptelkov")
print("")
time.sleep(2)

algus = int(input("1. ALUSTA MÄNGU 2. LOAD 3. EXIT 4.PEIDETUD JÄRGMINE PEATÜKK"))
print()
if algus == 4:
    print("EI SAA SEDA MÄNGIDA KUI POLE STEAMI")
    print("MÄNGIMISEKS TULEB MAKSTA 59.99$")
    int(input("SISESTAGE OMA PANGAKAARDI ANDMED: "))
    input("SISESTAGE OMA VANUS: ")
    
    exit()

def displayIntro():
    print("")
    print("Sa kadusid metsas ära.")
    print("Kõnnid metsas ringi ja järsku näed ühte mahajäetud lossi.")
    print("Hakkas sadama padukat ja sa otsustasid lossi jääda ööseks, et hommikul edasi liikuda.")
    print("Astusid sisse ja nägid seal kahte tuba")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Millise toa sa valid? (1 või 2): ")

    return path

def checkPath(chosenPath):
    print("Kõnnid mööda pikka koridori tuppa.")
    time.sleep(2)
    
   
    print()
    time.sleep(2)
    


    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("Mööda koridori tuppa kõndides näed sa palju vanu pilte ja esemeid ning kuuled kummalisi häälitsusi.")
        print("Järsult tuleb sul kananahk peale ja tekib tunne nagu keegi vaataks sind...")
        print("Sa tunned et keegi vaatab sind tagant ja vaatad selja taha... ")
        print("Korraga sa kuuled et keegi jookseks sinu poole... ")
        print("Jooksu hääled jõuavad aina lähemale ja lähemale...")
        print("Paanitsedes näed sa kardinat ja otsustad selle taha peitu minna.")
        print("")
        print("Tubli! Sa jõudsid peitu minna, oleks väga kurb kui sa oleksid hiljaks jäänud...")
        print("Sa tunnetad ei taha siia lossi kauemaks jääda, seega jooksed võimalikult kiiresti siit minema kuna sa ei soovi kauem selles lossis koos TEMAGA olla...")
        print("Lossist pääsedes oli juba vara hommik ja päike hakkas üles tõusma, sa kõnnid mööda metsa lootes et sa leida kodutee...")
        print("Korraga sa näed kaupmeest kes läheb linna ja küsid talt metsas oleva lossi kohta.")
        print("Kaupmees vaatas hirmunud näoga ja ütles, et nii paljud inimesed on sinna läinud kuid keegi pole tagasi tulnud...")
        print("Uudishimuga kuulates küsisid kes seal lossis elab... ")
        print("Kaupmees vastas karjatades: VALGE DAAM!!!")
        print("")
    else:
        print("Sa otsustasid et lähed teise tuppa")
        print("Järsult tuleb sul kananahk peale ja tekib tunne nagu keegi vaataks sind...")
        print("Sa tunned et keegi vaatab sind tagant ja vaatad selja taha... ")
        print("Korraga sa kuuled et keegi jookseks sinu poole... ")
        print("Jooksu hääled jõuavad aina lähemale ja lähemale...")
        print("Paanitsedes näed sa kardinat ja otsustad selle taha peitu minna...")
        print("")
        print("Sa kuuled et sammud muutusid valjemaks ja kiiremaks, sa ei jõudnud peitu minna...")
        print("Kui sammude omanik jõudis sulle lähemale tuli kuu pilvede tagant välja ja sa nägid kes see on... ")
        print("See on VALGE DAAM, sa olid nii hirmunud et sa ei tundnud oma jalgu ja ei suutnud ära joosta...")
        print("Valge daam tuli aina lähemale ja lähemale...")
        print("Peale seda kui Valge daam su kätte sai müüris ta su seina sisse tema asemele, et lossi needus püsiks.")
        print("")
        


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Kas sa soovid mängida veel korra? (jah või ei): ")