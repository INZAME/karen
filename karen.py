#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from core.utils.ip import Info
from core.decoder.zyxel_tools import Zyxel
import core.misc.design as design
import os
import colorama
import sys


def main():
    design.clear()
    zyxel = Zyxel()
    info = Info()
    try:
        kukold = zyxel.scramble_decode('0yxEdDYcrlZtQZzLOy+VxFQf')
    except Exception:
        print(design.FAILED_COLOUR + "[!] Error decoding password")
    print(design.BANNER_COLOUR + design.KAREN_BANER)
    if len(info.Values()) > 2:
        info.Print()
    else:
        print(design.FAILED_COLOUR + "[!] Error merging iface info")
        input('')
        sys.exit()
    if input('\nCorrect? [Y/n]: ') in design.YES:
        design.ISP_INFO('zxcd456', kukold)
        design.AP_INFO('My Wifi XD', 'wifi-password')

if __name__ == '__main__':
    try:
        main()
        print("\n")
    except KeyboardInterrupt:
        print(design.ERROR_COLOUR + "\n[!] Exiting util\n")
    input('')
