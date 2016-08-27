# -*- coding: utf-8 -*-
u"""Flask routes

:copyright: Copyright (c) 2016 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function
import flask
import celery
import celery.states
import os
import rncelery.tasks
import sys
import threading

app = flask.Flask(__name__)

@app.route('/start')
def app_start():
    _Celery()
    _Celery.all_status()
    return ''


@app.route('/status')
def app_status():
    _Celery.all_status()
    return ''


class _Celery(object):
    _task = []
    _lock = threading.Lock()

    def __init__(self):
        with self._lock:
            self.async_result = rncelery.tasks.start_simulation.apply_async(
                queue='rncelery',
            )
            self._task.append(self)
            _msg('{}: started', self.async_result.task_id)

    @classmethod
    def all_status(cls):
        """Job is actually running"""
        with cls._lock:
            for self in cls._task:
                self._status()

    def _status(self):
        res = self.async_result
        tid = self.async_result.task_id
        if not res or res.ready():
            _msg('{}: stopped', tid)
            self.__class__._task.remove(self)
            return
        _msg('{}: ready={} state={}', tid, res.ready(), res.state)


def _msg(fmt, *args):
    sys.stderr.write(('[{}] ' + fmt + '\n').format(os.getpid(), *args))
