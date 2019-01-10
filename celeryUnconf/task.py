import time

__author__ = 'Darr_en1'


from celery import Celery

app = Celery('my_task',
             # broker='amqp://darren:123456@192.168.98.129/darren',
             broker='redis://192.168.98.129:6379/1',
             backend='redis://192.168.98.129:6379/2'
             )

@app.task
def add(x,y):
    print(f'running {x}+{y}...')
    time.sleep(4)
    return x+y
