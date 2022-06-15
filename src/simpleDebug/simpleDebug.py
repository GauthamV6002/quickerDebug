from inspect import getframeinfo, stack
from termcolor import colored
import os


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
                       f"on_{status_clr}", attrs=['bold'])
        file = colored(filePath, attrs=['underline'])
        root_function = "exec()"

        msg = kwargs.get("msg", "")
        print(
            f'{status}\t|SAP CALL|\t{line}, in {file} at {root_function}\t{msg}')

    def sap(self, status="DEBUG", color=None, showFullPath=False, **kwargs):
        kwargs["status"] = status
        kwargs["showFullPath"] = showFullPath
        kwargs["color"] = color
        self.simpleAutoPrint(**kwargs)


sd = SimpleDebug()
sd.sap("TRACE")
