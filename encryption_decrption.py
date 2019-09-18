# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import Crypto.Random
from Crypto.Cipher import AES
import hashlib


SALT_SIZE = 16

NO_OF_ITERATIONS = 20

AES_MULTIPLE = 16



def generate_key(password,salt,iterations):
    assert iterations > 0
    
    key = password + salt