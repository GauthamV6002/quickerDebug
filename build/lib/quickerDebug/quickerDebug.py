from inspect import getframeinfo, stack
from termcolor import colored
import os
import time
import math
from types import ModuleType, FunctionType
import threading


class QuickerDebug:
    def __init__(self, **kwargs):
        self.startTime = time.perf_counter()
        self.simpleAutoPrintIndex = 0
        self.simpleAutoVarsIndex = 0
        self.trackedIndices = {}
        self.typeColors = kwargs.get("typeColors", {
            "int": "green",
            "float": "green",
            "complex": "green",
            "str": "yellow",
            "bool": "red",
            "list": "blue",
            "tuple": "cyan",
            "set": "cyan",
            "frozenset": "cyan",
            "dict": "magenta"
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
        self.simpleAutoVarsConfigs = {}

    def getTimestamp(self, t):
        mins = math.floor((t - self.startTime)/60)
        secs = (t - self.startTime) - mins*60
        return f"{mins}:{secs}"

    def getLineFileInfo(self, showFullPath, clr, **kwargs):
        caller = kwargs.get("caller", getframeinfo(stack()[-1][0]))
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
            f'{index}  {timestamp}    {status}    |AUTOPRINT CALL|    {lnf}\t{msg}')
        self.simpleAutoPrintIndex += 1

    def p(self, status="DEBUG", msg="", color=None, showFullPath=False, **kwargs):
        kwargs["status"] = status
        kwargs["showFullPath"] = showFullPath
        kwargs["color"] = color
        kwargs["msg"] = msg
        self.simpleAutoPrint(**kwargs)

    # autoVars config setter
    def vc(self, slot, *filters, **kwargs):
        self.simpleAutoVarsConfigs[slot] = (filters, kwargs)

    def simpleAutoVars(self, config_slot=None, **kwargs):
        color = kwargs.get("color", "cyan")
        index = colored(f"[V{self.simpleAutoVarsIndex}]",
                        "grey", attrs=['dark'])
        timestamp = colored(self.getTimestamp(
            time.perf_counter()), attrs=["reverse"])

        lnf = self.getLineFileInfo(kwargs.get("showFullPath", False), color)

        # Creates vars from globals by removing dunders, functions and modules
        filters = self.simpleAutoVarsConfigs[config_slot][0] if config_slot else kwargs.get(
            "filter", None)
        if(filters):
            autoVars = {k: v for k, v in globals().items() if k in filters}
        else:
            autoVars = {k: v for k, v in globals().items() if not(
                (k.startswith("__") and k.endswith("__")) or callable(v) or isinstance(v, ModuleType))}

        sidebar = colored(' ', color, attrs=['reverse'])
        joiner = (", " if kwargs.get("inline", False) else f"\n{sidebar} ")

        formattedAutoVars = joiner.join(
            [f"{k} = {colored(v, self.typeColors.get(type(v).__name__, 'grey'))}" for k, v in autoVars.items()])

        print(
            f'{sidebar} {index}  {timestamp}   |VARS CALL|    {lnf}\n{sidebar} {str(formattedAutoVars)}')

        self.simpleAutoVarsIndex += 1

    def v(self, slot=None, **kwargs):
        if slot == None:
            self.simpleAutoVars(**kwargs)
        elif (not slot in self.simpleAutoVarsConfigs):
            raise Exception(
                f"Auto Var Config Error: Slot \"{slot}\" was not found. Ensure that you've used pd.vc(slot) to create the respective configuration")
        else:
            self.simpleAutoVars(
                slot, **({**self.simpleAutoVarsConfigs[slot][1], **kwargs}))

    def track(self, var, delay, duration=None, **kwargs):
        self.trackedIndices[var] = 0
        autoclear = kwargs.get("autoclear", False)

        def printTrackInfo(varName, delay, duration, caller, autoclear):
            startTime = time.perf_counter()
            while True:
                index = colored(
                    f'[T{self.trackedIndices[varName]}]', "grey", attrs=["dark"])
                lnf = self.getLineFileInfo(False, "magenta", caller=caller)
                clr_val = colored(
                    f'{varName} = {globals()[varName]}', "magenta")
                print(
                    f'{index}    {clr_val}    {self.getTimestamp(time.perf_counter())}    |TRACK|    {lnf}')
                if autoclear:
                    os.system('cls||clear')
                self.trackedIndices[varName] += 1
                time.sleep((delay / 1000))
                if(duration):
                    if (time.perf_counter() - startTime) > duration:
                        break

        t = threading.Thread(target=printTrackInfo,
                             args=(var, delay, duration, getframeinfo(stack()[-1][0]), autoclear))
        t.start()

        # Real Time Tracker Preset
    def rt(self, var, **kwargs):
        self.track(var, 1, **kwargs)
