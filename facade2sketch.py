import cv2
import os

def pencil_sketch(img_rgb):
    """Briland Note: Re-wrote the original function from the PencilSketch Class
        due to License issues. Kept only the necessary transformation bits.
    """
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)
       
    return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)

entries = os.listdir('glass/')

for item in entries:
    if ".jpg" in item:
        print(item)
        img_rgb = cv2.imread("glass/" + item)
        img_pencil = pencil_sketch(img_rgb=img_rgb)
        cv2.imwrite("sketches/" + item, img_pencil)