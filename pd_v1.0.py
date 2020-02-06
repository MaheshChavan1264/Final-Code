from __future__ import print_function
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from imutils.object_detection import non_max_suppression
import numpy as np
import imutils
import cv2


# import loadimage
def openfile(param):
    global filename
    filename = filedialog.askopenfilename(title="Open file")
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(param, image=render)
    img.image = render
    img.place(x=0, y=30)

def pedDetection(param):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    image = cv2.imread(filename)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()
    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.05)
    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (142, 150, 255), 2)
    # show some information on the number of bounding boxes
    print("[INFO] {}: {} original boxes, {} after suppression".format(
        filename, len(rects), len(pick)))
    # show the output images
    cv2.imwrite('1.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    load = Image.open("1.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(param, image=render)
    img.image = render
    img.place(x=800, y=20)


root = Tk()
root.geometry("700x400")
root.title("Pedestrian Detection")
load = Image.open("Welcome.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=9, y=0)


def firstPage():
    root.destroy()
    global firstpage
    firstpage = Tk()
    firstpage.geometry("700x400")
    mylabel2 = Label(firstpage, text="Pedestrian Detection", font=("Helvetica", 26), bg="black", fg="white")
    mylabel2.pack()
    imagedetection = Button(firstpage, text="From Image", command=imageDetection, font=("verdana", 26), fg="red")
    imagedetection.place(x=230, y=230)
    videodetection = Button(firstpage, text="From Video", command=videoDetection, font=("verdana", 26), fg="red")
    videodetection.place(x=230, y=130)
    firstpage.mainloop()


def destroyfirstPage():
    firstpage.destroy()


def videodetection():
    pass


def videoDetection():
    startpage = Tk()
    startpage.state('zoomed')
    startdetection = Button(root, text="startCapturing", command=videodetection)
    startdetection.place(xrange=0, y=0)

    startpage.mainloop()


def captureImage(param):
    import time
    import picamera
    global filename
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        # camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('2.jpg', resize=(681, 483))
    load = Image.open("2.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(param, image=render)
    img.image = render
    img.place(x=0, y=20)


def imageDetection():
    destroyfirstPage()
    imagedetection = Tk()
    imagedetection.state('zoomed')

    def destroyImageDetection():
        imagedetection.destroy()

    loadimage = Button(imagedetection, text='Load Image', command=lambda: [openfile(imagedetection)])
    loadimage.place(x=0, y=0)
    captureimage = Button(imagedetection, text='Capture Image', command=lambda: [captureImage(imagedetection)])
    captureimage.place(x=70, y=0)
    detection = Button(imagedetection, text="Detect Human", command=lambda: [pedDetection(imagedetection)],
                       font=("verdana", 20))
    detection.pack(side=BOTTOM)
    closebutton = Button(imagedetection, text="Close", command=destroyImageDetection)
    closebutton.place(x=1320, y=0)
    imagedetection.mainloop()


start = Button(root, text="Start", command=firstPage, font="verdana, 15")
start.place(x=320, y=345)
root.mainloop()
