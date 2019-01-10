import time

__author__ = 'Darr_en1'
from celeryConf import app


@app.task
def add(x, y):
    print(f'running {x}+{y}...')
    time.sleep(4)
    return x + y
