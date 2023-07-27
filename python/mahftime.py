# importing whole module
from tkinter import *
from tkinter.ttk import *
from datetime import datetime 
  
# creating tkinter window
root = Tk()
root.title('Mahftime')
 
# This function is used to
# display time on the label

def mahftime():
    dt = datetime.now()
    hour= dt.strftime("%H")
    minute = dt.strftime("%M:%S")

    if int(hour) >=6 and int(hour)<= 24 :
        mahfhour = int(hour)-5
        if mahfhour >12:
            mahfhour = mahfhour-12
            ltnt="night"
        else:
            mahfhour=mahfhour
            ltnt= "light"
    else:
        mahfhour = int(hour)+24
        mahfhour = mahfhour-12
        ltnt= "night"
    
    
    time = str(mahfhour)+":"+ minute+" "+ltnt
    string = time
    lbl.config(text=string)
    lbl.after(1000, mahftime)
    


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='#454545',
            foreground='#A1CCD1')
 
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')

mahftime()
 
root.mainloop()