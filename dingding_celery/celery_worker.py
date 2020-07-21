__author__ = 'Darr_en1'

# ! /usr/bin/env python # coding: utf-8
import requests
import json
import time
from dingding_celery.config import HOST_IP, NOTIFY_URL, MOBILE_NUMBER

from celery import Celery

BROKER_URI = 'redis://%s:6379/6' % HOST_IP
BACKEND_URI = 'redis://%s:6379/5' % HOST_IP
worker = Celery('celery_worker', broker=BROKER_URI, backend=BACKEND_URI)

@worker.task
def notify_dingding(msg):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    post_data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "atMobiles": [MOBILE_NUMBER]
        }
    }
    r = requests.post(NOTIFY_URL, headers=headers, data=json.dumps(post_data))
    print(r.content)

from celery.schedules import crontab

worker.conf.update(timezone='Asia/Shanghai', enable_utc=True, beat_schedule={
    "morning_msg_1": {
        "task": "celery_worker.notify_dingding",
        "schedule": crontab(minute=0, hour=7),
        "args": ("早，起床了哟，先去做个早饭吧",)
                      },
    "morning_msg_2": {
        "task": "celery_worker.notify_dingding",
        "schedule": crontab(minute=30, hour=7),
        "args": ("我就问问你在干活咩?",)
    }
})
