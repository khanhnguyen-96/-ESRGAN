import sys
import os
from glob import glob
from PIL import ImageDraw, Image

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.progress_bar import ProgressBar  # noqa: E402

filePath = "C:/Users/LTT/OneDrive - K3v/Documents/LVTN/Dataset/demo/HR/*"
resultPath = "C:/Users/LTT/OneDrive - K3v/Documents/LVTN/Dataset/demo/HR_withScores/"

fileList = sorted(glob(filePath))
pbar = ProgressBar(len(fileList))

for index, value in enumerate(fileList):
    pbar.update("Read {}".format(value))
    # Read image
    img = Image.open(value, "r")

    # Draw text
    d = ImageDraw.Draw(img)
    d.text((10, 10), "Hello World", fill=(255, 255, 0))
    d.text((10, 20), "Hello World", fill=(255, 255, 0))
    d.text((10, 30), "Hello World", fill=(255, 255, 0))

    img.save(resultPath + os.path.basename(value))

print("Completed!")
