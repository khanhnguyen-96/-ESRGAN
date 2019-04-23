from PIL import ImageDraw
import cv2

img = cv2.imread("C:/Users/LTT/OneDrive - K3v/Documents/LVTN/Dataset/demo/HR")

d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(255, 255, 0))

img.save("pil_text.png")
