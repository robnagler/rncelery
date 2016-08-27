# -*- coding: utf-8 -*-
u"""Flask routes

:copyright: Copyright (c) 2016 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function
from pykern.pkdebug import pkdc, pkdexc, pkdp
import flask
import celery
import celery.states
import rncelery.tasks
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
    _task = {}
    _lock = threading.Lock()

    def __init__(self):
        with self._lock:
            self.async_result = rncelery.tasks.start_simulation.apply_async()
            tid = self.async_result.task_id
            self._task[tid] = self
            pkdp('{}: started', tid)

    @classmethod
    def all_status(cls):
        """Job is actually running"""
        with cls._lock:
            for tid in cls._task:
                cls._status(tid)

    @classmethod
    def _status(cls, tid):
        try:
            self = cls._task[tid]
        except KeyError:
            pkdp('{}: not found', tid)
            return
        res = self.async_result
        if not res or res.ready():
            pkdp('{}: stopped', tid)
            return
        pkdp('{}: ready={} state={}', tid, res.ready(), res.state)
