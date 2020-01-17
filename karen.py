#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from core.misc.design import *
from core.utils.ip import Info
from core.decoder.zyxel_tools import Zyxel
import os
import colorama
import sys

colorama.init(autoreset=True) # Reset colours

def main():
    os.system('cls')
    zyxel = Zyxel()
    info = Info()
    kukold = zyxel.scramble_decode('0yxEdDYcrlZtQZzLOy+VxFQf')
    print(BANNER_COLOUR + KAREN_BANER)
    if len(info.Values()) > 2:
        info.Print()
    else:
        print(FAILED_COLOUR + "[!] Error merging iface info")
        input('')
        sys.exit()
    if input('\nCorrect? [Y/n]: ') in YES:
        ISP_INFO('zxcd456', kukold)
        AP_INFO('My Wifi XD', 'wifi-password')

if __name__ == '__main__':
    try:
        main()
        print("\n")
    except KeyboardInterrupt:
        print(ERROR_COLOUR + "\n[!] Exiting util\n")
    input('')