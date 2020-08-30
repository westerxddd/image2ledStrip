import numpy
from PIL import Image
from rpi_ws281x import *
import time
from datetime import datetime
import math

LED_COUNT      = 116      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 128     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_OFFSET = 6

FOR_ITERATIONS = 10

def colorWipe(strip, color):
    for i in range(0,120):
        strip.setPixelColor(i, color)
    strip.show()    

filename='US_flag_h.jpg'
# filename = 'izery.jpg'
# filename = 'park_solacki.jpg'
# filename = 'Star_Wars_Logo.jpg'

img = Image.open(filename).convert('RGB')
origWidth, origHeight = img.size
ratio = origWidth/origHeight

newWidth = math.ceil(120*ratio)
img.thumbnail((int(newWidth), 120))
pixels = img.load()
width, height = img.size

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()   

startdate = datetime.now().strftime("%H:%M:%S")
print(startdate)
for row in range(0, width):
    for x in range(0, height):
        r,g,b = pixels[row,x]
        strip.setPixelColor(x+LED_OFFSET, Color(r, g, b))
    strip.show()
    time.sleep(0.01)

startdate = datetime.now().strftime("%H:%M:%S")
print(startdate)
colorWipe(strip, Color(0,0,0))
