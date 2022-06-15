from enum import auto
from inspect import getframeinfo, stack
from termcolor import colored
import os
import time
import math
from types import ModuleType, FunctionType

a = 1
b = "hello"
x = True
my_var = 23.42

my_dict = {"a": 1, "b": 2, "c": 3}
l = [1, 2, 3, 4, 5]
s = {1, 2, 3}
t = (2, 3, 4)


class SimpleDebug:
    def __init__(self, **kwargs):
        self.startTime = time.perf_counter()
        self.simpleAutoPrintIndex = 0
        self.simpleAutoVarsIndex = 0
        self.typeColors = kwargs.get("typeColors", {
            "int": "green",
            "float": ("green", "dark"),
            "complex": "green",
            "string": "yellow",
            "bool": "blue"
        })
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

    def getLineFileInfo(self, showFullPath, clr):
        caller = getframeinfo(stack()[-1][0])
        filePath = os.path.basename(
            caller.filename) if not showFullPath else caller.filename
        line = colored(f"Ln {caller.lineno}", "white", f"on_{clr}")
        file = colored(filePath, attrs=['underline'])
        return f'{line}, in {file}'

    def simpleAutoPrint(self, **kwargs):
        index = colored(f"[P{self.simpleAutoPrintIndex}]",
                        "grey", attrs=['dark'])
        timestamp = colored(self.getTimestamp(
            time.perf_counter()), attrs=["reverse"])

        status = kwargs.get("status", "DEBUG")
        if kwargs["color"] != None:
            status_clr = kwargs["color"]
        else:
            status_clr = status_clr = self.statusColors.get(status, "green")
        status = colored(status, status_clr)

        lnf = self.getLineFileInfo(kwargs["showFullPath"], status_clr)

        msg = kwargs.get("msg", "")
        if msg != "":
            msg = "Message: " + \
                colored(kwargs.get("msg", ""), "grey", attrs=['bold'])

        print(
            f'{index}  {timestamp}    {status}    |SAP CALL|    {lnf}\t{msg}')
        self.simpleAutoPrintIndex += 1

    def p(self, status="DEBUG", msg="", color=None, showFullPath=False, **kwargs):
        kwargs["status"] = status
        kwargs["showFullPath"] = showFullPath
        kwargs["color"] = color
        kwargs["msg"] = msg
        self.simpleAutoPrint(**kwargs)

    def simpleAutoVars(self, **kwargs):
        index = colored(f"[V{self.simpleAutoVarsIndex}]",
                        "grey", attrs=['dark'])
        timestamp = colored(self.getTimestamp(
            time.perf_counter()), attrs=["reverse"])

        lnf = self.getLineFileInfo(kwargs.get(
            "showFullPath", False), kwargs["clr"])

        # Creates vars from globals by removing dunders, functions and modules
        autoVars = {k: v for k, v in globals().items() if not(
            (k.startswith("__") and k.endswith("__")) or callable(v) or isinstance(v, ModuleType))}

        if kwargs["inline"]:
            sidebar = colored(' ', kwargs['clr'], attrs=['reverse'])
            formattedAutoVars = f", ".join(
                [f"{k} = {v}" for k, v in autoVars.items()])
            print(
                f'{sidebar} {index}  {timestamp}   |VARS CALL|    {lnf}\n{sidebar} {str(formattedAutoVars)}')
        else:
            sidebar = colored(' ', kwargs['clr'], attrs=['reverse'])
            # Formats with a join
            formattedAutoVars = f"\n{sidebar} ".join(
                [f"{k} = {v}" for k, v in autoVars.items()])
            print(
                f'{sidebar} {index}  {timestamp}   |VARS CALL|    {lnf}\n{sidebar} {str(formattedAutoVars)}')

        self.simpleAutoVarsIndex += 1

    def v(self, inline=False, clr="cyan", **kwargs):
        kwargs["inline"] = inline
        kwargs["clr"] = clr
        self.simpleAutoVars(**kwargs)


sd = SimpleDebug()
sd.v(True)
