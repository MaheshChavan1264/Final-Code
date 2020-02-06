from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title('Branch Filter')
root.geometry("598x120+250+100")

filename=""
def browsefunc():
    global filename
    filename = filedialog.askopenfilename()
    return filename


ttk.Label(root, text="Select Your File (Only RAW files)").grid(row=0, column=0, sticky='e')
bButton = ttk.Button(root, text="Browse", command=browsefunc).grid(row=3, column=0, sticky='w')

root.mainloop()
print(bButton)