# Iride Date Extract function
#
# Copyright Emanuele Parini
#
# Call: IrideNumber(pattern)

import re
import cv2
import pytesseract

def IrideNumber():
    img = cv2.imread('upload/numero.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    tesseract_config = r'--user-words words/number_words.txt --psm 6'
    data = pytesseract.image_to_string(img, lang="ita", config=tesseract_config)

    clean = "".join(re.split("[^0-9-./]*", data))
    return clean
