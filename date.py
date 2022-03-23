# Iride Date Extract function
#
# Copyright Emanuele Parini
#
# Call: IrideDate(pattern)

import re
import cv2
import pytesseract

def IrideDate(pattern):
    img = cv2.imread('upload/data.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    tesseract_config = r'-c tessedit_char_whitelist=0123456789-/. tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz --psm 6'
    data = pytesseract.image_to_string(thresh, lang="ita", config=tesseract_config)

    found = re.search(pattern, data).group(1)
    return found