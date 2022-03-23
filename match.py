# Iride Match function
#
# Copyright Emanuele Parini
#
# Call: IrideMatch(user_id)

import cv2
import numpy as np
import os

def IrideMatch(user_id):
    threshold = 0.8  # set threshold
    headerDirectory = os.fsencode('loghi/' + user_id)

    img_rgb = cv2.imread('upload/test.jpg')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    for headerFile in os.listdir(headerDirectory):
        headerFilename = os.fsdecode(headerFile)
        template = cv2.imread('loghi/' + user_id + '/' + headerFilename, 0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        if len(loc[0]):
            for pt in zip(*loc[::-1]):
                return headerFilename.replace(".jpg", "")
                break
