
from barcode import Code128
from barcode.writer import ImageWriter
import os
from PIL import Image
import win32api
import time
import pyautogui

i = 1
while i < 20000:
    number = input("barcode:")
    my_code = Code128(number)
    with open("some.png", "wb") as f:
        Code128(number, writer=ImageWriter()).write(f)
    im = Image.open("some.png")
    angle = 90
    out = im.rotate(angle, expand=True)
    out.save('some2.png')
    os.startfile("some2.png", "print")
    time.sleep(1)
    pyautogui.click(x=100, y=200)
    time.sleep(1)
    #label = create_label(qlr, im, label_size='38x90.3', threshold=70, cut=True, rotate=0)
