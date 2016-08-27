# -*- coding: utf-8 -*-
"""Runs the server in uwsgi or http modes

:copyright: Copyright (c) 2015 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
from __future__ import absolute_import, division, print_function
import rncelery.server

def default_command():
    rncelery.server.app.run(host='0.0.0.0', port=8000, debug=1, threaded=True)
