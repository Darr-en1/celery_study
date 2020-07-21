# from __future__ import absolute_import
#
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from datetime import timedelta

from celery.schedules import crontab


__author__ = 'Darr_en1'

BROKER_URL = 'redis://192.168.98.128:6379/1'


CELERY_RESULT_BACKEND = 'redis://192.168.98.128:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入任务模块
CELERY_IMPORTS = (
    'celeryConf.addTask',
    'celeryConf.mulTask',
)

CELERYBEAT_SCHEDULE = {
    'addTask': {
        'task': 'celeryConf.addTask.add',
        'schedule': timedelta(seconds=10),
        'args': (4, 4)
    },
    'mulTask': {
        'task': 'celeryConf.mulTask.mul',
        'schedule': crontab(hour=18, minute=10),
        'args': (4, 4)
    }
}

# app.conf.beat_schedule = {
#     'period_add_task': {  # 计划任务
#         'task': 'celeryConf.addTask.add',  # 任务路径
#         'schedule': crontab(hour=18, minute=16, day_of_week=1),
#         'args': (3, 4),
#     },
#     'add-every-30-seconds': {  # 每10秒执行
#         'task': 'celeryConf.addTask.mul',  # 任务路径
#         'schedule': 10.0,
#         'args': (4, 4)
#     },
# }

# sender.add_periodic_task(
#     crontab(hour=7, minute=30, day_of_week=1),
#     test.s('Happy Mondays!'),
# )
# 由于最新的celery4.2不支持windows系统，因此按照网上的建议安装了3.1.25版。按照官网的说明使用
