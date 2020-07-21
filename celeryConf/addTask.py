import time

from celery import Task

__author__ = 'Darr_en1'
from celeryConf import app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class demotask(Task):

    def on_success(self, retval, task_id, args, kwargs):  # 任务成功执行
        logger.info('task id:{} , arg:{} , successful !'.format(task_id, args))

    def on_failure(self, exc, task_id, args, kwargs, einfo):  # 任务失败执行
        logger.info('task id:{} , arg:{} , failed ! erros : {}'.format(task_id, args, exc))

    def on_retry(self, exc, task_id, args, kwargs, einfo):  # 任务重试执行
        logger.info('task id:{} , arg:{} , retry !  einfo: {}'.format(task_id, args, exc))


@app.task(base=demotask)
def add(x, y):
    print(f'running {x}+{y}...')
    time.sleep(4)
    return x + y


@app.task(bind=True)  # 绑定任务
def add_(self, x, y):
    logger.info(self.request.__dict__)  # 打印日志
    try:
        a = []
        a[10] == 1
    except Exception as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)  # 出错每5秒尝试一次，总共尝试3次
    return x + y
