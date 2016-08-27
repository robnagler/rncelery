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

_JID = 1

app = flask.Flask(__name__)

@app.route('/start', methods=('GET'))
def app_start():
    # _Celery().jid
    return 'hello'


@app.route('/status/<jid>', methods=('GET'))
def app_status(jid):
    return jid


class _Celery(object):
    _job = {}
    _lock = threading.Lock()

    def __init__(self):
        global _JID
        with self._lock:
            self.jid = _JID++;
            self.in_kill = False
            self._job[self.jid] = self
            self.data = data
            self._job[self.jid] = self
            self.async_result = None
            # This command may blow up
            self.async_result = self._start_job()

    @classmethod
    def is_processing(cls, jid):
        """Job is either in the queue or running"""
        with cls._lock:
            return bool(cls._find_job(jid))

    @classmethod
    def is_running(cls, jid):
        """Job is actually running"""
        with cls._lock:
            self = cls._find_job(jid)
            if self is None:
                return False
            return self.async_result.status in (celery.states.STARTED, celery.states.RECEIVED)


    @classmethod
    def _find_job(cls, jid):
            try:
                self = cls._job[jid]
            except KeyError:
                return None
            res = self.async_result
            if res:
                pkdp('{} {} {} {}', jid, res, res.ready(), res.state)
            if not res or res.ready():
                del self._job[jid]
                return None
            return self

    def _start_job(self):
        return rncelery.tasks.start_simulation.apply_async(args=[])
