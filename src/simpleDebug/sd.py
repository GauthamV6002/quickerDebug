from inspect import getframeinfo, stack
from termcolor import colored
import os
import time
import math


class SimpleDebug:
    def __init__(self, **kwargs):
        self.startTime = time.perf_counter()
        self.statusColors = kwargs.get("statusColors", {
            "OFF": "magenta",
            "O": "magenta",
            "ERROR": "red",
            "ERR": "red",
            "E": "red",
            "WARNING": "yellow",
            "WARN": "yellow",
            "W": "yellow",
            "DEBUG": "green",
            "D": "green",
            "INFO": "blue",
            "I": "blue",
            "TRACE": "cyan",
            "T": "cyan",
        })

    def getTimestamp(self, t):
        mins = math.floor((t - self.startTime)/60)
        secs = (t - self.startTime) - mins*60
        return f"{mins}:{secs}"

    def simpleAutoPrint(self, **kwargs):
        timestamp = colored(self.getTimestamp(
            time.perf_counter()), "grey", "on_white", attrs=["dark"])

        status = kwargs.get("status", "DEBUG")
        if kwargs["color"] != None:
            status_clr = kwargs["color"]
        else:
            status_clr = status_clr = self.statusColors.get(status, "green")
        status = colored(status, status_clr)

        caller = getframeinfo(stack()[-1][0])
        filePath = os.path.basename(
            caller.filename) if not kwargs["showFullPath"] else caller.filename
        line = colored(f"Ln {caller.lineno}", "white",
                       f"on_{status_clr}")
        file = colored(filePath, attrs=['underline'])

        msg = kwargs.get("msg", "")
        if msg != "":
            msg = "Message: " + \
                colored(kwargs.get("msg", ""), "grey", attrs=['bold'])

        print(f'{timestamp}    {status}    |SAP CALL|    {line}, in {file}\t{msg}')

    def p(self, status="DEBUG", msg="", color=None, showFullPath=False, **kwargs):
        kwargs["status"] = status
        kwargs["showFullPath"] = showFullPath
        kwargs["color"] = color
        kwargs["msg"] = msg
        self.simpleAutoPrint(**kwargs)


sd = SimpleDebug()
sd.p()
