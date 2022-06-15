import traceback
# from termcolor import colored

# SAP Call Format:
# *STATUS*  |SAP CALL|   Ln *LINE*, Col *Column* in *FILE*  at  *ROOT_FUNCTION*   *INFO_OPT*

# ie.,
# ERR_CRITICAL  |SAP CALL|  Ln 28, Col 23 in main.py  at run()    "a function lol"

class SimpleDebug:
    def __init__(self):
        pass

    def simpleAutoPrint(self, **kwargs):
        status = kwargs.get("status", "LOG")
        msg = kwargs.get("msg", "")
        line = 23
        col = 12
        file = "main.py"
        root_function = "run()"
        print(f'{status}\t|SAP CALL|\tLn {line}, col {col} in {file}. At {root_function}\t{msg}')

    def sap(self, **kwargs):
        self.simpleAutoPrint(**kwargs)

sd = SimpleDebug()
sd.sap()