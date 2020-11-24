import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd1in54_V2
from PIL import Image,ImageDraw,ImageFont
import time

epd = EPD()
epd.init()
epd.Clear(0xFF)

image = Image.new('1', (epd.width, epd.height), 255)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
draw.rectangle((0, 10, 200, 34), fill = 0)
draw.text((8, 12), 'hello world', font = font, fill = 255)
draw.text((8, 36), u'mytest', font = font, fill = 0)
draw.line((16, 60, 56, 60), fill = 0)
draw.line((56, 60, 56, 110), fill = 0)
draw.line((16, 110, 56, 110), fill = 0)
draw.line((16, 110, 16, 60), fill = 0)
draw.line((16, 60, 56, 110), fill = 0)
draw.line((56, 60, 16, 110), fill = 0)
draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
draw.rectangle((16, 130, 56, 180), fill = 0)
draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
epd.display(epd.getbuffer(image.rotate(90)))
time.sleep(2)  
epd.sleep()