import pyautogui
from PIL import Image
import TImage


class SSImage:
    def __init__(self, image, rd, cd):
        self.image = image
        self.rd = rd
        self.cd = cd



    def split(self):
        timages = []
        for i in range(len(self.rd)-1):
            left = self.rd[i]
            right = self.rd[i+1]
            for j in range(len(self.cd)-1):
                upper = self.cd[j]
                lower = self.cd[i+1]
                image = self.image.crop((left, upper, right, lower))
                timages.append(TImage.from_image(image))
        return timages





