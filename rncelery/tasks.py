# -*- coding: utf-8 -*-
"""Celery tasks

:copyright: Copyright (c) 2016 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function
from celery import Celery
import time

celery = Celery('rncelery')

celery.conf.update(
    BROKER_URL='amqp://guest@localhost//',
    CELERYD_CONCURRENCY=1,
    CELERYD_LOG_COLOR=False,
    CELERYD_MAX_TASKS_PER_CHILD=1,
    CELERYD_PREFETCH_MULTIPLIER=1,
    CELERY_ACKS_LATE=True,
    CELERY_REDIRECT_STDOUTS=False,
    CELERY_RESULT_BACKEND = 'rpc',
    CELERY_RESULT_PERSISTENT=True,
    CELERY_TASK_PUBLISH_RETRY=False,
    CELERY_TASK_RESULT_EXPIRES=None,
    CELERY_TRACK_STARTED=True,
)

@celery.task
def start_simulation():
    time.sleep(10)
