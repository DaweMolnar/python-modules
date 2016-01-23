#!/usr/bin/env python2
"""Watchdog module"""
from threading import Timer

class Watchdog(object):
    """Watchdog class. Usage:
    Watchdog([timeout],[function to call on timeout])"""
    def __init__(self, timeout, user_handler=None):  # timeout in seconds
        self.timeout = timeout
        self.handler = user_handler if user_handler is not None \
		    else self.default_handler
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def reset(self):
        """Resets the watchdog to restart the timer"""
        self.timer.cancel()
        self.timer = Timer(self.timeout, self.handler)
        self.timer.start()

    def stop(self):
        """Stop the timer"""
        self.timer.cancel()

    @classmethod
    def default_handler(cls):
        """If no function set to call at timeout
		default_handler is called and raise an exception"""
        raise
