########################
#      ülesanne06      #
#     Dajana Mähdi     #
#      15.02.2022      #
########################

#nimekiri
erakonnad = []
re, kesk, koku = 0, 0, 0
with open('sobrad.txt','r') as sobrad:
    for rida in sobrad:
        enimi,pnimi,er, likes = rida.split(" ")
        print(f"{enimi:11} {pnimi:11} {er:4} {likes:5}",end="")
        if er=="RE":
            re+=1
        elif er=="KE":
            kesk+=1
            
        #lisan massiivi kui pole masiivis
            
print(erakonnad)            
print("\n------------------")
print(f"Reformikad: {re}\nKesikud: {kesk}\n")
print(f"Erakondi kokku: {len(erakonnad)}")
            
            
            
            