####################
#    ülesanne9     #
#   dajana mähdi   #
#    17.02.2022    #
####################

#kuupäev
import datetime

ik = "38011062222"
aasta = int("19"+ik[1]+ik[2])
kuu = int(ik[3]+ik[4])
paev = int(ik[5]+ik[6])

sp = datetime.date(aasta, kuu, paev)

print(sp)




#kuupäeva ül
import datetime

kuud = ["jaanuar","veebruar","märts"]
aeg = datetime.datetime.now()
print(aeg.strftime("%d.%B %Y "))

print(aeg.strftime("%d.")+kuud[int(aeg.strftime("%m"))-1]+aeg.strftime(" %Y "))




