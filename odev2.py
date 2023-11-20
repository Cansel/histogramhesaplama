# -*- coding: utf-8 -*-
"""odev2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OFvZHg5qh8wxZj5dDOeBfkRrwkchJBfS
"""

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
while True:
    ret, frame = kamera.read()#Kameradan bir görüntü alıyor.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#BGR renk uzayını HSV renk uzayına çevirir.

    #alt_kırmızı, üst_kırmızı kırmızı renk aralığınnı gösterir.
    alt_kırmızı = np.array([0, 100, 100])
    üst_kırmızı = np.array([10, 255, 255])
    kırmızı_mask = cv2.inRange(hsv, alt_kırmızı, üst_kırmızı) #Kırmızı rengi maskeler.

    #alt_yeşil, üst_yeşil yeşil renk aralığını gösterir.
    alt_yesil = np.array([30, 30, 30])
    üst_yesil = np.array([100, 255, 255])
    yesil_mask = cv2.inRange(hsv, alt_yesil, üst_yesil) #Yeşil rengi maskeler.

    #alt_mavi, üst_mavi mavi renk aralığını gösterir.
    alt_mavi = np.array([90, 50, 50])
    üst_mavi = np.array([120, 255, 255])
    mavi_mask = cv2.inRange(hsv, alt_mavi, üst_mavi) #Mavi rengi maskeler.


    #bitwise_and() komutu ile yeşil,mavi rengi siyahlaştırma yapılıyor.
    result_frame = cv2.bitwise_and(frame, frame, mask=~(yesil_mask | mavi_mask))


    cv2.imshow("İlk hali frame", frame) #imshow() komutu ile görüntünün ilk halini gösteriyor.
    cv2.imshow("Sonraki hali maskelenmiş", result_frame) #imshow() komutu ile görüntünün ilk halini gösteriyor.



    if cv2.waitKey(1) & 0xFF == ord("q"):#waitkey() içine yazılan değer kadar süre bekler, 'q' ya basınca görüntü durur.
        break

kamera.release()
cv2.destroyAllWindows()