"""
Copy paste from https://github.com/hoffstadt/DearPyGui/issues/2212
"""

import os
import sys

from dearpygui import dearpygui as dpg


class CyrillicSupport:
    # Parameters for Cyrillic conversion
    big_let_start = 0x00C0  # Capital "А" in Cyrillic.
    big_let_end = 0x00DF  # Capital "Я" in Cyrillic.
    small_let_end = 0x00FF  # Little "я" in Cyrillic
    remap_big_let = 0x0410  # Initial number for the reassigned Cyrillic alphabet

    alph_len = (
        big_let_end - big_let_start + 1
    )  # adds a shift from large letters to small ones
    alph_shift = (
        remap_big_let - big_let_start
    )  # adds a transition from reassignment to non-reassignment

    def __init__(self, app_path):
        self.app_path = app_path

        # Path to the font file
        font_file = self.app_path / "resources/UbuntuMono-Regular.ttf"
        # print(font_file, font_file.is_file())
        self.font_path = os.path.join(self.app_path, "fonts", font_file)

    def registry_font(self):
        with dpg.font_registry():
            with dpg.font(self.font_path, size=18) as self.font:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

                dpg.add_font_range(0x0391, 0x03C9)  # Greek character range
                dpg.add_font_range(
                    0x2070, 0x209F
                )  # Range of upper and lower numerical indices

                # Fixing keyboard input on Windows
                if sys.platform == "win32":
                    self._remap_chars()

                # Set font
                dpg.bind_font(self.font)

    def _remap_chars(self):
        biglet = (
            self.remap_big_let
        )  # Initial number for the reassigned Cyrillic alphabet
        for i1 in range(
            self.big_let_start, self.big_let_end + 1
        ):  # Cyclic switching of large letters
            dpg.add_char_remap(i1, biglet)  # Reassigning the big letter
            dpg.add_char_remap(
                i1 + self.alph_len, biglet + self.alph_len
            )  # Reassign a small letter
            biglet += 1  # choose the next letter

        # The letters "Ёё" must be added separately, since they are located elsewhere in the table
        dpg.add_char_remap(0x00A8, 0x0401)
        dpg.add_char_remap(0x00B8, 0x0451)

    def decode_string(self, instr: str):
        if sys.platform == "win32":
            outstr = []
            for i in range(0, len(instr)):
                char_byte = ord(instr[i])
                if char_byte in range(self.big_let_start, self.small_let_end + 1):
                    char = chr(ord(instr[i]) + self.alph_shift)
                    outstr.append(char)
                # Checking for "Ё"
                elif char_byte == 0x00A8:
                    char = chr(0x0401)
                    outstr.append(char)
                # Checking for "ё"
                elif char_byte == 0x00B8:
                    char = chr(0x0451)
                    outstr.append(char)
                else:
                    outstr.append(instr[i])

            return "".join(outstr)

        else:
            return instr
