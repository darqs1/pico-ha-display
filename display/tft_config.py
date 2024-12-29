from machine import Pin, SPI
from time import sleep_ms
from libs.st7789py import ST7789

TFA = 1
BFA = 3
WIDE = 0
TALL = 0
SCROLL = 0      # orientation for scroll.py
FEATHERS = 1    # orientation for feathers.py

def config(rotation=0):
    """
    Configures and returns an instance of the ST7789 display driver.

    Args:
        rotation (int): The rotation of the display (default: 0).

    Returns:
        ST7789: An instance of the ST7789 display driver.
    """

    return ST7789(
        SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19), miso=None),
        240,
        320,
        reset=Pin(21, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=rotation)