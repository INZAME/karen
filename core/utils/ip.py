# -*- coding: utf-8 -*- 

import netifaces
from core.misc.design import *

class Info:

    def __init__(self):
        self.interface = []
        try:
            gateway_info    = netifaces.gateways()[netifaces.AF_INET][0]
            default_gateway = gateway_info[0]
            interface_id    = gateway_info[1]
            iface           = netifaces.ifaddresses(interface_id)[netifaces.AF_INET][0]
        except Exception:
            pass
        else:
            self.interface.extend((iface['addr'], iface['netmask'], default_gateway))
                   
    def Print(self):
        template = '| {:<10} {:<24} {}'
        padding = ' ' * 5
        print(padding + SECTION_COLOUR + "** [ LOCAL INFO ] **")
        print('+{:-<28}+'.format(''))
        print(template.format('Local IP:', SUCESS_COLOUR + self.interface[0], BANNER_COLOUR + '|'))
        print(template.format('Netmask:', SUCESS_COLOUR + self.interface[1], BANNER_COLOUR + '|'))
        print(template.format('Router IP:', SUCESS_COLOUR + self.interface[2], BANNER_COLOUR + '|'))
        print('+{:-<28}+'.format(''))

    def Values(self):
        return self.interface