#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import sys 

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

if __name__ == '__main__':
    
    try:
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
        if sys.argv[1] == 'blue':
            blue = Color(10,150,100)
            for i in range(strip.numPixels()):
             strip.setPixelColor(i, blue)
             strip.show()
             time.sleep(30/1000)

        elif sys.argv[1] == "clear":
            for i in range(strip.numPixels()):
             strip.setPixelColor(i,Color(0,0,0))
             strip.show()
             time.sleep(5/1000)
    except KeyboardInterrupt:
        for i in range(strip.numPixels()):
            strip.setPixelColor(i,Color(0,0,0))
            strip.show()
        
