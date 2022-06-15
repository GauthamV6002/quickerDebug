from inspect import getframeinfo, stack
import traceback
from colorama import Fore, Style


class SimpleDebug:
    def __init__(self, **kwargs):
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

    def simpleAutoPrint(self, **kwargs):
        status = kwargs.get("status", "LOG")
        msg = kwargs.get("msg", "")
        caller = getframeinfo(stack()[-1][0])
        line = caller.lineno
        file = caller.filename
        root_function = "exec()"
        print(f'{status}\t|SAP CALL|\tLn {line} in {file} at {root_function}\t{msg}')

    def sap(self, status="LOG", **kwargs):
        kwargs.status = status
        self.simpleAutoPrint(**kwargs)


sd = SimpleDebug()
sd.sap()
