# -*- coding: utf-8 -*- 
#
# Zyxel (NDMS V2) decoder/encoder
# author: Felis-Sapiens
#

import sys
from base64 import b64decode, b64encode
from hashlib import md5

class Zyxel:

    def _first_step(self, password, x1, x2):
        x1 &= 0xff
        x2 &= 0xff
        for i in range(len(password)):
            password[i] = (password[i] ^ x2) & 0xff
            x2, x1 = x1 + x2, x2
        return password

    def _second_step(self, password):
        x = 0
        for b in password:
            x ^= b
        for i in range(1,8):
            a = ((x >> i) ^ (~x << i)) & 0xff
            x = ((a << i) ^ (~a ^ x)) & 0xff
        for i in range(len(password)):
            password[i] ^= x
        return password


    def scramble_decode(self, password):
        '''
        Decode password string
        '''
        if len(password) % 4 != 0:
            password += '=' * (4 - len(password) % 4)
    
        password = list(b64decode(password))
        length = len(password)
        if length not in [0x12, 0x24, 0x48]:
            raise ValueError('Invalid input length!')
    
        a2 = length // 7
        x2 = password[a2]
        del password[a2]
    
        a1 = x2 % (length - 1)
        x1 = password[a1]
        del password[a1]
    
        password = self._second_step(password)
        password = self._first_step(password, x1, x2)
    
        zero_pos = password.index(0)
        if zero_pos != -1:
            length = zero_pos
        return bytes(password[:length]).decode()

    def scramble_encode(self, password):
        '''
        Encode password string
        '''
        if password == '':
            raise ValueError('Password is empty!')
        old_length = len(password)
        length = len(password) + 3
        if length < 0x13:
            length = 0x12
        elif length < 0x25:
            length = 0x24
        elif length < 0x49:
            length = 0x48
        else:
            raise ValueError('Password is too long!')
    
        password = password.encode()
        md5_digest = md5(password).digest()
    
        password = list(password)
        if length != old_length:
            password.append(0)
            for i in range(old_length+1, length-2):
                password.append((password[i-old_length-1] * 2 + md5_digest[2 + i%14]) & 0xff)
    
        x1 = md5_digest[0]
        x2 = md5_digest[1]
        password = self._first_step(password, x1, x2)
        password = self._second_step(password)
        password.insert(x2 % (length - 1), x1)
        password.insert(length // 7, x2)
        return b64encode(bytes(password)).decode('utf-8')
