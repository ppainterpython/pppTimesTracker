import datetime
import tkinter as tk
from te import TimeEntry
#import tkinter.ttk as ttk
start2 = datetime.datetime(2025,1,20,13)
stop2 = datetime.datetime(2025,1,20,14, 5)
# te1 = TimeEntry()
te2 = TimeEntry(start2, stop2, "learning", "Place notes here", 0.0)


root = tk.Tk()
root.geometry("800x500")
root.title("PP Python Time Tracker")
# label = tk.Label(root,text="Hello World!", font=('Ariel', 18))
# label.pack()
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="Hello World!").grid(column=0, row=0)
tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
