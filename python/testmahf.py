import tkinter as tk
from tkinter.ttk import *
from datetime import datetime
import win32gui

root = tk.Tk()

# Make the window transparent
root.wm_attributes("-transparentcolor", "#454545")

# Remove the title bar
root.overrideredirect(True)

# Create a style object
style = Style()
style.configure("Custom.TFrame", background="#454545")

# Rest of your code remains unchanged...

# Rest of your code remains unchanged...

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()



# create fake title bar
title_bar = Frame(root, style="Custom.TFrame", relief="raised")#border=0)
title_bar.pack(expand=1, fill="x")

# bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# create title text
title_label = Label(title_bar, text="MahfTime",font=('calibri', 10, 'bold'), background="#454545", foreground="#A1CCD1")
title_label.pack(side="left")# pady=4)

# create close button on titleBar
close_label = Label(title_bar, text="  c   ", background="#454545", foreground="#A1CCD1", relief="raised")# border=0.5)
close_label.pack(side="right")# pady=0)
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
    lbl.after(1000, mahftime)


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
