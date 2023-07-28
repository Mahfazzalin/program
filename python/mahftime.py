# importing whole module
from tkinter import *
from tkinter.ttk import *
from datetime import datetime

# creating tkinter window
root = Tk()
root.geometry("277x91")
root.overrideredirect(True)  # remove title bar

# Create a style object
style = Style()

# Set the background color for the Frame
style.configure("Custom.TFrame", background="#454545")


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()


# create fake title bar
title_bar = Frame(root, style="Custom.TFrame", relief="raised", border=0)
title_bar.pack(expand=0, fill=X)

# bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# create title text
title_label = Label(title_bar, text="MahfTime", background="#454545", foreground="white")
title_label.pack(side=LEFT, pady=2)

# create close button on titleBar
close_label = Label(title_bar, text="  X   ", background="#454545", foreground="white", relief="raised", border=0)
close_label.pack(side=RIGHT, pady=0)
close_label.bind("<Button-1>", quitter)


# This function is used to
# display time on the label
def mahftime():
    dt = datetime.now()
    hour = dt.strftime("%H")
    minute = dt.strftime("%M:%S")

    if int(hour) >= 7 and int(hour) <= 24:
        mahfhour = int(hour) - 6
        if mahfhour > 12:
            mahfhour = mahfhour - 12
            ltnt = "night"
        else:
            mahfhour = mahfhour
            ltnt = "light"
    else:
        mahfhour = int(hour) + 24
        mahfhour = mahfhour - 18
        ltnt = "night"

    time = str(mahfhour) + ":" + minute + " " + ltnt
    string = time
    lbl.config(text=string)
    lbl.after(100, mahftime)


# Styling the label widget so that clock
# will look more attractive
lbl = Label(root, font=('calibri', 40, 'bold'),
            background='#454545',
            foreground='#A1CCD1')

# Placing clock at the center
# of the tkinter window
lbl.pack(anchor='center')

mahftime()
# root.wm_attributes('-fullscreen', 'False')
root.mainloop()
