__author__ = 'Darr_en1'

from celery import Celery

app = Celery('celery_conf')  # name

app.config_from_object('celeryConf.config')  # setting
