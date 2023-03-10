import numpy as np
import cv2 as cv
import PIL
import imutils
from tkinter import ttk
from tkinter import *
from scipy import ndimage as ndi
from skimage.filters import edges
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
from PIL import ImageTk, Image
from copy import deepcopy


class MainSolution():
    def __init__(self):
        self.image = cv.imread("image.jpg")
        self.imgray = None
        self.trsh1 = None
        self.trsh2 = None

    def filt(self):
        self.imgray = cv.cvtColor(cv.pyrMeanShiftFiltering(
            self.image, 15, 50), cv.COLOR_BGR2GRAY)
        img = Image.fromarray(self.imgray)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def global_threshold(self):
        ret, thresh1 = cv.threshold(self.imgray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        self.trsh1 = deepcopy(thresh1)
        img = Image.fromarray(thresh1)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def adaptive_threshold(self):
        thresh2 = cv.adaptiveThreshold(self.imgray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        self.trsh2 = deepcopy(thresh2)
        img = Image.fromarray(thresh2)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def negative(self):
        negativeimg = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        negative = abs(255-negativeimg)
        img = Image.fromarray(negative)
        img = img.resize((300,300))
        return ImageTk.PhotoImage(img)

    def multiply(self):
        im = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        negative = abs(im)
        img = Image.fromarray(negative*2)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def pow2(self):
        im = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
        negative = abs(im)
        img = Image.fromarray(negative*negative)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def linear_contrast(self):
        minVal, maxVal, a, b = cv.minMaxLoc(self.imgray)
        minVal, maxVal, a, b = cv.minMaxLoc(self.imgray)
        max_type = 255
        a = max_type / (maxVal - minVal)
        image_of_doubles = a * (self.imgray - minVal)
        image_of_doubles = PIL.Image.fromarray(image_of_doubles)
        img = image_of_doubles.resize((300, 300))
        return ImageTk.PhotoImage(img)



if __name__ == "__main__":
    root = Tk()
    ms = MainSolution()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"1400x700")

    lbl_text1 = ttk.Label(text="???????????????????? ?????????????????? ??????????????????")
    lbl_text1.place(x=250, y=10)
    img1 = ms.filt()
    lbl1 = ttk.Label(image=img1)
    lbl1.image = img1
    lbl1.place(x=30, y=40, width=300, height=300)
    img2 = ms.global_threshold()
    lbl2 = ttk.Label(image=img2)
    lbl2.image = img2
    lbl2.place(x=370, y=40, width=300, height=300)

    lbl_text2 = ttk.Label(text="???????????????????? ?????????????????? ??????????????????")
    lbl_text2.place(x=90, y=360)
    img3 = ms.adaptive_threshold()
    lbl3 = ttk.Label(image=img3)
    lbl3.image = img3
    lbl3.place(x=30, y=390, width=300, height=300)

    lbl_text3 = ttk.Label(text="??????????????")
    lbl_text3.place(x=480, y=360)
    img4 = ms.negative()
    lbl4 = ttk.Label(image=img4)
    lbl4.image = img4
    lbl4.place(x=370, y=390, width=300, height=300)

    lbl_text4 = ttk.Label(text="?????????????????? ???? ??????????????????")
    lbl_text4.place(x=750, y=10)
    img5 = ms.multiply()
    lbl5 = ttk.Label(image=img5)
    lbl5.image = img5
    lbl5.place(x=700, y=40, width=300, height=300)

    lbl_text5 = ttk.Label(text="???????????????????? ?? ??????????????")
    lbl_text5.place(x=750, y=360)
    img6 = ms.pow2()
    lbl6 = ttk.Label(image=img6)
    lbl6.image = img6
    lbl6.place(x=700, y=390, width=300, height=300)

    lbl_text6 = ttk.Label(text="???????????????? ????????????????????????????????")
    lbl_text6.place(x=1100, y=10)
    img7 = ms.linear_contrast()
    lbl7 = ttk.Label(image=img7)
    lbl7.image = img7
    lbl7.place(x=1050, y=40, width=300, height=300)

    root.mainloop()
