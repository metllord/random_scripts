#!python
# -*- coding: utf-8 -*-

# Time Tracker: use this to measure how much time you devote to a task.

import datetime
import sys


class TimeTracker(object):
    def __init__(self, task):
        self.start_time = datetime.datetime.now()
        self.task = task

    def document(self):
        with open('tasks.txt', 'a') as out:
            out.write('{time} - {task}'.format())
