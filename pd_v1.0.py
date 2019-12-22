from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry("700x400")
root.title("Pedestrian Detection")
load = Image.open("Welcome.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=9, y=0)

def firstPage():
    startpage = Tk()
    startpage.geometry("700x400")
    mylabel = Label(startpage, text= "What you want", font=("Helvetica", 26), bg="black", fg = "white")
    mylabel.pack()
    mylabel2 = Label(startpage, text="Pedestrian Detection from Images", font=("Helvetica", 26),bg="black", fg = "white")
    mylabel2.pack()
    imagedetection = Button(startpage, text = "Image Detection", command=imageDetection, font =("verdana", 26),fg = "red")
    imagedetection.pack()
    mylabel3 = Label(startpage, text="Or", font=("Helvetica", 30),bg="black", fg = "white")
    mylabel3.pack()
    mylabel4 = Label(startpage, text="Pedestrian Detection from Video", font=("Helvetica", 26),bg="black", fg = "white")
    mylabel4.pack()
    videodetection = Button(startpage, text = "video Detection", font =("verdana", 26), command=videoDetection, fg = "red")
    videodetection.pack()
    startpage.mainloop()


def imageDetection():
    startpage = Tk()
    startpage.state('zoomed')
    def loadImage():
        path1 = filedialog.askopenfilename(initialdir='/', title="Select Image",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        load = Image.open(path1)
        render = ImageTk.PhotoImage(load)
        img = Label(startpage, image=render)
        img.image = render
        img.place(x=0, y=20)

    loadimage = Button(startpage, text="Load the Image", command=loadImage, font=("verdana", 16))
    loadimage.place(x=0,y=0)

    startpage.mainloop()

def videoDetection():
    startpage = Tk()
    startpage.state('zoomed')

    startpage.mainloop()


start = Button(root, text="Start", command=firstPage, font="verdana, 15")
start.place(x=320, y=345)

root.mainloop()
