__author__ = 'Darr_en1'
from celeryUnconf.task import add

if __name__ == '__main__':
    print("start")
    print(f"4+6={add.delay(4,6)}")
    print("end")
