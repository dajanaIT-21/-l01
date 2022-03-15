#5
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("300x300")

#funktsioonid
def arvuta():
    hind = sisestus.get()
    
    #print("Tere " +nimi)
    valjund.config(text=hind)

#sildid
silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)
silt = Label(aken, text="Käibemaksu määr:")
silt.grid(row=1,column=0)
silt = Label(aken, text="-------------------------")
silt.grid(row=3,columnspan=2)
silt = Label(aken, text="Käibemaks:")
silt.grid(row=4,column=0)
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
valjund = Label(aken, text="0.00€")
valjund.grid(row=4,column=1)
#mingi nupp
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=arvuta)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=20, command=arvuta)
valikukast.grid(row=2,column=1)

#sisestusväljad
silt = Label(aken, text="Hind käibemaksuga:")
silt.grid(row=5,column=0)
valjund = Label(aken, text="0.00€")
valjund.grid(row=5,column=1)
#nupud
nupp1 = Button(aken, text="ok", width=10, command=arvuta)
nupp1.grid(row=7, column=1)

aken.mainloop()



