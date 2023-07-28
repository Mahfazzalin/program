from tkinter import *
from tkinter.ttk import *
from datetime import datetime

root = Tk()

# Set transparency (alpha) value for the window (0: fully transparent, 1: fully opaque)
root.attributes('-alpha', 0.1)  # You can adjust the value to your desired transparency level

# Remove the title bar
root.overrideredirect(True)

# Create a style object
style = Style()
style.configure("Custom.TFrame", background="darkgreen")

# Rest of your code remains unchanged...


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
        mahfhour = mahfhour - 12
        ltnt = "night"

    time = str(mahfhour) + ":" + minute + " " + ltnt
    string = time
    lbl.config(text=string)
    lbl.after(1000, mahftime)

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def quitter(e):
    root.quit()


# create fake title bar
title_bar = Frame(root, style="Custom.TFrame", relief="raised", border=1)
title_bar.pack(expand=1, fill=X)

# bind the title bar
title_bar.bind("<B1-Motion>", move_app)

# create title text
title_label = Label(title_bar, text="MahfTime", background="darkgreen", foreground="white")
title_label.pack(side=LEFT, pady=4)

# create close button on titleBar
close_label = Label(title_bar, text="  X   ", background="darkgreen", foreground="white", relief="raised", border=1)
close_label.pack(side=RIGHT, pady=4)
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
