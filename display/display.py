import display.tft_config as tft_config
import libs.st7789py as st7789

import fonts.vga1_8x16 as mono_font
import fonts.NotoSans_32 as noto_sans
import fonts.NotoSerif_32 as noto_serif
import fonts.NotoSansMono_32 as noto_mono

from time import sleep

class Display:

    def __init__(self) -> None:
        self.tft = tft_config.config(tft_config.WIDE)
        self.tft.inversion_mode(False)
        self.tft.fill(st7789.BLACK)
        self.line = 0
    
    def center(self, string, line=0, color=st7789.WHITE):
        """
        Centers the given string horizontally on the screen at the specified row.

        Args:
            font: The font to use for rendering the string.
            string: The string to be centered.
            row: The row where the string will be displayed.
            color: The color of the string (default: st7789.WHITE).

        Returns:
            None
        """
        if line == 0:
            line = self.line

        screen = self.tft.width  # get screen width
        width = self.tft.write_width(noto_sans, string)  # get the width of the string
        col = self.tft.width // 2 - width // 2 if width and width < screen else 0
        self.tft.write(noto_sans, string, col, line, color)  # and write the string

        # # example
        # self.tft.write(noto_sans, "Temperatura: " , 1 , row, st7789.WHITE)
        self.line += line + noto_sans.HEIGHT

        # # center the name of the first font, using the font
        # center(noto_sans, "0", row, st7789.RED)
        # row += noto_sans.HEIGHT

    def typewriter(self, text, col=1, line=0):
        if line == 0:
            line = self.line

        for letter in text:
            self.tft.text(mono_font, letter, col, line, st7789.WHITE, st7789.BLACK)
            col += mono_font.WIDTH
            self.tft.text(mono_font, " ", col, line, st7789.BLACK, st7789.WHITE)
            sleep(0.1)

        self.tft.text(mono_font, " ", col, line, st7789.WHITE, st7789.BLACK)
        self.line = line + mono_font.HEIGHT
    
    def print(self, text, col=1, line=0):
        if line == 0:
            line = self.line
        self.tft.text(mono_font, text, col, line, st7789.WHITE, st7789.BLACK)
        self.line = line + mono_font.HEIGHT

    def blink(self, col, line):
        for i in range(0,10):
            self.tft.text(mono_font, " ", col, line, st7789.BLACK, st7789.WHITE)
            sleep(0.5)
            self.tft.text(mono_font, " ", col, line, st7789.WHITE, st7789.BLACK)
            sleep(0.5)

    def clear(self):
        self.line = 0
        self.tft.fill(st7789.BLACK)


