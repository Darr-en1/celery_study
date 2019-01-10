__author__ = 'Darr_en1'

from celeryConf.addTask import add
from celeryConf.mulTask import mul

print('start................')
add.delay(4,6)
mul.delay(4,6)
print('end..................')
