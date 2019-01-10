from datetime import timedelta

from celery.schedules import crontab

__author__ = 'Darr_en1'

BROKER_URL = 'redis://192.168.98.129:6379/1'

CELERY_RESULT_BACKEND = 'redis://192.168.98.129:6379/2'

#导入任务模块
CELERY_IMPORTS=(
    'celeryConf.addTask',
    'celeryConf.mulTask',
)

CELEYBEAT_SCHEDULE={
    'addTask':{
        'task':'celeryConf.addTask.add',
        'schedule':timedelta(seconds=10),
        'args':(4,4)
    },
    'mulTask':{
        'task':'celeryConf.mulTask.mul',
        'schedule':crontab(hour=18,minute=10),
        'args':(4,4)
    }
}
