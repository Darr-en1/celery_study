#!/usr/bin/python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from celeryConf.addTask import add
from celeryConf.mulTask import mul

__author__ = 'Darr_en1'

print('start................')
add.delay(4, 8)
mul.delay(4, 10)
print('end..................')
