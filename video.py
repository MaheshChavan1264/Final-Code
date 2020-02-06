
def videodetection():
    pass

    startpage = Tk()
    startpage.state('zoomed')
    startdetection = Button(root, text="startCapturing", command=videodetection)
    startdetection.place(xrange=0,y=0)

    startpage.mainloop()