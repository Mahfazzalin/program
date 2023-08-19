import tkinter as tk
from tkinter.ttk import *
from datetime import datetime

root = tk.Tk()
root.wm_attributes("-transparentcolor", "#454545")
root.overrideredirect(True)

style = Style()
style.configure("Custom.TFrame", background="#454545")

def move_app(e):
    dx = e.x_root - x_clicked
    dy = e.y_root - y_clicked
    x = root.winfo_x() + dx
    y = root.winfo_y() + dy
    root.geometry(f"+{x}+{y}")

def quitter(e):
    root.quit()

def on_title_click(event):
    global x_clicked, y_clicked
    x_clicked = event.x
    y_clicked = event.y

title_bar = Frame(root, style="Custom.TFrame", relief="raised", border=1)
title_bar.pack(expand=1, fill="x")

title_label = Label(title_bar, text="MahfTime", background="#454545", foreground="white", font=('calibri', 18, 'bold'))
title_label.pack(side="left", pady=4)
title_label.bind("<B1-Motion>", move_app)
title_label.bind("<Button-1>", on_title_click)

close_label = Label(title_bar, text="  X   ", background="#454545", foreground="white", relief="raised", border=1)
close_label.pack(side="right", pady=0)
close_label.bind("<Button-1>", quitter)

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
    title_label.config(text=time)
    root.after(1000, mahftime)

mahftime()
root.mainloop()
