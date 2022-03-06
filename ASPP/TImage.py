import pyautogui
from pynput import mouse
import pytesseract


class TImage:
    def __init__(self, image, text):
        self.image = image
        self.text = text


def get_bbox():
    bbx = []
    bby = []
    canceled = False

    def on_click(x, y, button, pressed):
        nonlocal canceled
        if button == mouse.Button.right:
            canceled = True
            return False

        bbx.append(x)
        bby.append(y)
        if not pressed:
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    if canceled:
        return False

    return min(bbx), min(bby), abs(bbx[0]-bbx[1]), abs(bby[0]-bby[1])


def from_drag():
    bbox = get_bbox()
    im = pyautogui.screenshot(region=bbox)
    text = pytesseract.image_to_string(im)
    return TImage(im, text)


def from_image(image):
    text = pytesseract.image_to_string(image)
    return TImage(image, text)






