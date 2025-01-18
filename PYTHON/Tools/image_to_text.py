
# image to text
import pytesseract

# adds image processing capabilities
from PIL import Image

import os.path

scriptpath = os.path.dirname(__file__)
file = open('comic.txt', mode='w', encoding='utf-8')
paths = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
for i in range(1, 270):
    filename = os.path.join(scriptpath, f'DOWNLOADS\\{i}.jpg')
    img = Image.open(filename)

    # path where the tesseract module is installed
    pytesseract.pytesseract.tesseract_cmd = paths
    # converts the image to result and saves it into result variable
    text = pytesseract.image_to_string(img)
    # write text in a text file and save it to source path
    file.write(text)
    print(f'Loading {round(i*100/269,2)}%')
