#Mouse
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

#OCR
from PIL import Image
from PIL import ImageGrab
import pytesseract
#Här får du skriva in din egna grej
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/00oan01/AppData/Local/Tesseract-OCR/tesseract'


mouse = MouseController()
keyboard = KeyboardController()
#time.sleep(2)

print('The current pointer position is {0}'.format(mouse.position))
#De två under kan du använda för att kordinater
#time.sleep(3)
#print('The current pointer position is {0}'.format(mouse.position))

#Skriv in xy för ena hörnet och xy för andra här
im = ImageGrab.grab(bbox=(67, 209, 509, 350))
im.save('img.png')

img = Image.open('img.png')
result = pytesseract.image_to_string(img)
print(result)

#kordinater för var musen ska cklika för att googla
mouse.move(953, 167)
mouse.click(Button.left, 1)
keyboard.type(result)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
#(1392, 79)
