import random
import time


print("          Valge Daam")
print(" Mängu tegid kaks saamatut inimest")
print("Dajana Mähdi ja Remy Rasmus Koptelkov")
print("")
time.sleep(2)

algus = int(input("1.ALUSTA MÄNGU 2.EXIT 3.PEIDETUD JÄRGMINE PEATÜKK (NR): "))
print()

if algus == 1:
    print("------- ALGAB PARIM MÄNG -------")

elif algus == 2:
    exit()


if algus == 3:
    print("EI SAA SEDA MÄNGIDA KUI POLE STEAMI")
    print("MÄNGIMISEKS TULEB MAKSTA 59.99$")
    int(input("SISESTAGE OMA PANGAKAARDI ANDMED: "))
    input("SISESTAGE OMA VANUS: ")
    PRINT("Lmao imik")
    

def displayIntro():
    print("")
    print("Oma perega tülli minnes otsustasid metsa ära joosta...")
    print("Mõnda aega joostes kadusid sa metsas ära...")
    print("Kõnnid metsas ringi ja järsku näed ühte mahajäetud lossi.")
    print("Hakkas sadama padukat ja sa otsustasid lossi jääda ööseks, et hommikul edasi liikuda.")
    print("Astusid sisse ja nägid seal kahte pikka koridori.")
    print("Kuna sa tahtsid kiiremas korras koju tagasi saada pidid sa valima ainult ühe suuna...")
    print()

time.sleep(2)

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Millise suuna sa valid? (1 või 2): ")
    print()
    return path

time.sleep(2)

def checkPath(chosenPath):
    print("Kõnnid mööda pikka koridori tuppa.")
    time.sleep(2)
    
   
    print()
    
    


    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("Mööda koridori tuppa kõndides näed sa palju vanu pilte ja esemeid ning kuuled kummalisi häälitsusi.")
        print("Järsult tuleb sul kananahk peale ja tekib tunne nagu keegi vaataks sind...")
        print("Sa tunned et keegi vaatab sind tagant ja vaatad selja taha... ")
        print("Korraga sa kuuled et keegi jookseks sinu poole... ")
        print("Jooksu hääled jõuavad aina lähemale ja lähemale...")
        print("Paanitsedes näed sa kardinat ja otsustad selle taha peitu minna.")
        print("")
        
        time.sleep(2)
        
        print("Sa jõudsid kuidagi moodi peitu minna...")
        print("Sa tunnetad ei taha siia lossi kauemaks jääda, seega jooksed võimalikult kiiresti siit minema kuna sa ei soovi kauem selles lossis koos TEMAGA olla...")
        print("Lossist pääsedes oli juba vara hommik ja päike hakkas üles tõusma, sa kõnnid mööda metsa lootes et sa leida kodutee...")
        print("Korraga sa näed kaupmeest kes läheb linna ja küsid talt metsas oleva lossi kohta.")
        print("Kaupmees vaatas hirmunud näoga ja ütles, et nii paljud inimesed on sinna läinud kuid keegi pole tagasi tulnud...")
        print("Uudishimuga kuulates küsisid kes seal lossis elab... ")
        print("Kaupmees vastas karjatades: VALGE DAAM!!!")
        print("LÕPP")
        print("")
    else:
        print("Sa otsustasid et lähed teise tuppa")
        print("Kordidori lõppu jõudes näed sa ust ja otsustad sissse minna...")
        print("Sisse astudes näed sa armsalt sisestatud tuba, seinale vaadates näed sa plakatit mille peal oli kijutletud Mario ja ta näo ümber olid joonistatud südamed... ")
        print("Sa koheselt taipad et kesiganes siin ka ei elaks armastab Mariot ... ")
        print("Natuke aega mõeldes tuleb sul tahe plakat endale võtta ja kodus simpida ta üle...")
        print("Toas ringi vaadates näed sa kappi ja otsustad selle sisse vaadata...")
        print("Kapp lahti tehes näed sa Ghostbustersite vasustust ja võtad elle endale ...")
        print("")
        
        time.sleep(2)
        
        print("Toas ringi vaadates näed sa nugas pikka köit...")
        print("Natuke mõeldes otsustad sa köie abil aknast välja ronida... ")
        print("Aknast alla vaadates näed et tuba pole kõrgel, ainult 10-dal korrusel...")
        print("Sa seod köie enda ümber ja ronid akanst välja...")
        print("Pool tundi hiljem suudsid sa kuidagi maani jõuda...")
        print("Kuid kõik pole nii kerge angu tundus...") 
        print("Lossi seinte vahelt tuli välja mingi pooleldi läbipaistev elukas naise kujuga...")
        print("Sa õritasid sellest elukast jagu saada varustusega mille leidsid kapist, kuid sellest polnud kasu kuna sa ei osanud seda kasutada...")
        print("Elukas sai su kätte ja võttis su varustuse ära ja lõi sind nii tugevalt et sa kaotassid teaduse, seejärel tassis su lossi tagasi...")
        print("Üles ärgates näed et sa oled toas kus sa pole kunagi varem olnud, tuba oli täiesti tühi ja oli ainult kolm akent... ")
        print("Mõnda aega hiljem ilmub elukas tuppa ja sa küsid talt kes ta on ja mis ta nimi on...")
        print("Elukas vastab koriseva häälega: 'vAlGe DaAm'")
        print("Peale seda tõstab Valge daam su õhku ja paneb su seina sisse tema asemele, et ta saaks lõpuks vabaks...")
        print("Sellest hetkest saati on Valge daam vaba.")
        print("LÕPP")

time.sleep(2)

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Kas sa soovid mängida veel korra? (jah või ei): ")

   