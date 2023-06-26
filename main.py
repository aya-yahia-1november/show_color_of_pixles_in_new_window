import cv2
import numpy as np

def click_event(event, x, y, flag, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y, 1]
        red = img[x,y, 2]
        colored_img = np.zeros((512, 512, 3), dtype=np.uint8)
        colored_img[::]= [blue, green, red]
        cv2.imshow("color", colored_img)

img = cv2.imread("people_set.jpg", 1)
cv2.imshow("frame", img)
cv2.setMouseCallback("frame", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

