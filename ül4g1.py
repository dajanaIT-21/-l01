#4
from tkinter import *

#akna seaded
aken = Tk()
aken.title('"Kalkukas"')
aken.geometry("200x200")


#nupud
tekst=Label(aken, text="vastus siia:", font="Tahoma 12").grid(row=0, columnspan=4)
nupp1 = Button(aken, text="7", font="Tahoma 12", width=4)
nupp1.grid(row=1, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="8", font="Tahoma 12", width=4)
nupp2.grid(row=1, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="9", font="Tahoma 12", width=4)
nupp3.grid(row=1, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="/", font="Tahoma 12", width=4)
nupp4.grid(row=1, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="4", font="Tahoma 12", width=4)
nupp1.grid(row=2, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="5", font="Tahoma 12", width=4)
nupp2.grid(row=2, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="6", font="Tahoma 12", width=4)
nupp3.grid(row=2, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="*", font="Tahoma 12", width=4)
nupp4.grid(row=2, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="1", font="Tahoma 12", width=4)
nupp1.grid(row=3, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="2", font="Tahoma 12", width=4)
nupp2.grid(row=3, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="3", font="Tahoma 12", width=4)
nupp3.grid(row=3, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="-", font="Tahoma 12", width=4)
nupp4.grid(row=3, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="0", font="Tahoma 12", width=4)
nupp1.grid(row=4, column=0, padx=2, pady=2)
nupp2 = Button(aken, text=",", font="Tahoma 12", width=4)
nupp2.grid(row=4, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="=", font="Tahoma 12", width=4)
nupp3.grid(row=4, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="+", font="Tahoma 12", width=4)
nupp4.grid(row=4, column=3, padx=2, pady=2)


aken.mainloop()