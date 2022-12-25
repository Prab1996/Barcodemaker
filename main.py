import barcode

from barcode import Code128

from barcode.writer import ImageWriter

import os

import win32api

import time

import pyautogui

from PIL import Image, ImageDraw

from brother_ql.conversion import convert

from brother_ql.backends.helpers import send

from brother_ql.raster import BrotherQLRaster

 

i = 1

while i < 20000:

    number = input("barcode:")

    ean = barcode.get('code128', number, writer=ImageWriter())

    filename = ean.save("some4", {"module_width":0.583, "module_height":27.00})

 

    im = Image.open("some4.png")

    angle = 90

    out = im.rotate(angle, expand=True)

    out.save('some2.png')

    b = int(1)

    qr_image = Image.open('some4.png')

    label_images = []

    for i in range(b):

        im = Image.new("L", (991, 413), color = "white")

        im.paste(qr_image)

        label_images.append(im)

    backend = 'pyusb'    # 'pyusb', 'linux_kernal', 'network'

    model = 'QL-800'

    printer = 'usb://0x04f9:0x209b'

 

    qlr = BrotherQLRaster(model)

    qlr.exception_on_warning = True

 

    # Converting print instructions for the Brother printer

    instructions = convert(

            qlr=qlr,

            images=label_images,    #  Takes a list of file names or PIL objects.

            label='39x90',

            rotate='90',    # 'Auto', '0', '90', '270'

            threshold=70.0,    # Black and white threshold in percent.

            dither=False,

            compress=False,

            dpi_600=False,

            hq=True,    # False for low quality.

            cut=True

    )

 

    send(instructions=instructions, printer_identifier=printer, backend_identifier=backend, blocking=True)

    #os.startfile("some2.png", "print")

    #time.sleep(1)

    #pyautogui.click(x=1188, y=774)

    #time.sleep(1)
