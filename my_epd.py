import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd1in54_V2
from PIL import Image,ImageDraw,ImageFont
import time

epd = epd1in54_V2.EPD()
epd.init()
epd.Clear(0xFF)
while True:
    new_time = time.time()
    new_time = time.ctime(new_time)
    new_time = new_time.encode('GB2312')
    image = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    draw.text((8, 36), u'time', font = font, fill = 0)
    draw.text((20,12), u'by_huangyifan', font = font, fill = 0)
    draw.text((12,12), new_time, font = font, fill = 0)
    epd.display(epd.getbuffer(image.rotate(90)))
    time.sleep(0.1)
epd.sleep()

