# -*- coding: utf-8 -*- 

import textwrap
import colorama
from sys import version
from os import system

colorama.init(autoreset=True) # Reset colours

SUCESS_COLOUR   = colorama.Fore.GREEN   + colorama.Style.BRIGHT
FAILED_COLOUR   = colorama.Fore.RED     + colorama.Style.BRIGHT
BANNER_COLOUR   = colorama.Fore.WHITE   + colorama.Style.BRIGHT  
SECTION_COLOUR  = colorama.Fore.YELLOW  + colorama.Style.BRIGHT
ERROR_COLOUR    = colorama.Back.RED     + colorama.Style.BRIGHT

KAREN_BANER = textwrap.indent('''
 _   __  ___  ______ _____ _   _ 
| | / / / _ \ | ___ \  ___| \ | |
| |/ / / /_\ \| |_/ / |__ |  \| |
|    \ |  _  ||    /|  __|| . ` |
| |\  \| | | || |\ \| |___| |\  |
\_| \_/\_| |_/\_| \_\____/\_| \_/

        [Made by INZAME]
    [Decoder by Felis-Sapiens]
''', "")
YES=['', 'y', 'yes', 'Yes', u'д', u'да', u'Д']
PADDING_3 = '\n' + (' ' * 3)
PADDING_6 = '\n' + (' ' * 6)

def GAP_28():
    print('+{:-<28}+'.format(''))

def AP_INFO(ssid, password):
    print(PADDING_3 + SECTION_COLOUR + "** [ AP POINT INFO ] **")
    GAP_28()
    print('| {:<10} {:<15} |\n| {:<10} {:<15} |'.format('SSID: ', ssid, 'Password: ', password))
    GAP_28()

def ISP_INFO(login, password):
    print(PADDING_6 + SECTION_COLOUR + "** [ ISP INFO ] **")
    GAP_28()
    print('| {:<10} {:<15} |\n| {:<10} {:<15} |'.format('Login: ', login, 'Password: ', password))
    GAP_28()

def clear():
    if version == 'nt':
        system('cls')
    else:
        system('clear') 