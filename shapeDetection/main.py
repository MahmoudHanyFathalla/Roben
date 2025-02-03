import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
count_cr=0
count_rec=0
count_tr=0
count_line=0
img_rgb = cv.imread('C:\\Users\\hp\\Desktop\\smart\\img.jpg',cv.IMREAD_GRAYSCALE)
template_cr = cv.imread('C:\\Users\\hp\\Desktop\\smart\\cr.jpg',cv.IMREAD_GRAYSCALE)
template_rec = cv.imread('C:\\Users\\hp\\Desktop\\smart\\rec.jpg',cv.IMREAD_GRAYSCALE)
template_tr = cv.imread('C:\\Users\\hp\\Desktop\\smart\\tr.jpg',cv.IMREAD_GRAYSCALE)
template_line = cv.imread('C:\\Users\\hp\\Desktop\\smart\\line.jpg',cv.IMREAD_GRAYSCALE)
w, h = template_cr.shape[::-1]
res_cr = cv.matchTemplate(img_rgb,template_cr,cv.TM_CCOEFF_NORMED)
res_rec = cv.matchTemplate(img_rgb,template_rec,cv.TM_CCOEFF_NORMED)
res_tr = cv.matchTemplate(img_rgb,template_tr,cv.TM_CCOEFF_NORMED)
res_line = cv.matchTemplate(img_rgb,template_line,cv.TM_CCOEFF_NORMED)
threshold = 0.98
loc_cr = np.where( res_cr >= threshold)
loc_rec = np.where( res_rec >= threshold)
loc_tr = np.where( res_tr >= threshold)
loc_line = np.where( res_line >= threshold)
for pt in zip(*loc_cr[::-1]):
    count_cr += 1
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
for pt in zip(*loc_rec[::-1]):
    count_rec += 1
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
for pt in zip(*loc_tr[::-1]):
    count_tr += 1
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
for pt in zip(*loc_line[::-1]):
    count_line += 1
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)        
cv.imwrite('res.png',img_rgb)

print(count_cr)
print(count_rec)
print(count_tr)
print(count_line)