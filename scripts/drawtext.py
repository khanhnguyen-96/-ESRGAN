import sys
import os
from glob import glob
from PIL import ImageDraw, Image

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.progress_bar import ProgressBar  # noqa: E402

filePath = "C:/Users/LTT/OneDrive - K3v/Documents/LVTN/Dataset/demo/HR/*"
resultPath = "C:/Users/LTT/OneDrive - K3v/Documents/LVTN/Dataset/demo/HR_withScores/"


def drawResultDirectory(filePath, resultPath, *args):
    fileList = sorted(glob(filePath))
    pbar = ProgressBar(len(fileList))

    for index, value in enumerate(fileList):
        pbar.update("Read {}".format(value))
        # Read image
        img = Image.open(value, "r")

        img = drawResultFile(img, args)
        img.save(resultPath + os.path.basename(value))

    print("Completed!")


def drawResultFile(file, *args):
    d = ImageDraw.Draw(file)

    for i, score in enumerate(args):
        d.text((10, 10 * i), score, fill=(255, 255, 0))

    return file
