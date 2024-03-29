# Welcome to quickerDebug!

## ⚠️ Please note that this package is currently in development, and you may encounter frequent bugs (ironic for a debugging library, I know).

QuickerDebug offers a standardized alternative to `print("here")` and `print(my_var)` with simple, quick, and efficient logging functions that provide information without the need to repeat yourself. Generally, the best use case is for small scale applications or test code, where a complete debugger is overkill, but `print("here")` can get overly tedious to repeatedly type. Function names are purposefully shortened avoid writing out long function calls, so you don't waste time while debugging.

Note that quickerDebug is optimized for terminals supported colors (through `termcolor`), meaning it may not work on all CLIs.

## Installation

`>> pip install quickerDebug`

## Quick Start

#### Initialization

To use the package, you need to create an instance of `QuickerDebug`, from which methods can be called.

```python
from quickerDebug import quickerDebug
qd = quickerDebug.QuickerDebug()
```

#### Basic Logging

The two essential functions for logging are `qd.p()` and `qd.v()`.

```python
# Logs index, line number, timestamp, and a optional message
qd.p()

# qd.p() also supports positional arguments for extra functionality like so:
qd.p(status="DEBUG", msg="", color=None, showFullPath=False, **kwargs)
# ie
qd.p("INFO", "First Test", "blue", True)

# Logs all variables with thier current values
qd.v()

# Variables are displayed inline
qd.v(inline=True)
```

#### AutoVar Configs

AutoVar configs allow you to set up a list of varibles with a certain format to be printed with current values with the `qd.vc()` function, and then allows you to access that printing configuration with `qd.v(config_key)`.

```python
a = 1
b = 2
# Create a config that prints the variables a and b, where the config_key is 1
qd.vc(1, "a", "b")

# Would print just a & b
qd.v(1) # config_key is the first argument
```

#### Variable Tracking

`quickerDebug` also provides lightweight, real-time variable tracking in the terminal through `qd.track()` and `qd.rt()`

```python
a = 1

# Would print the value of a every 10ms for 5s
qd.track("a", 10, 5)

# Would clear the terminal after each print
qd.track("a", 10, 5, autoclear=True)

# Preset Function for indefinite real-time tracking
qd.rt("a")
```

#### Additional Keyword Arguments

All quickerDebug functions can take certain keyword arguments, as shown below:

| Function               | Kwargs                                    |
| ---------------------- | ----------------------------------------- |
| `qd.p()`               | `status : str `                           |
| `qd.p() & qd.v()`      | `showFullPath : bool `                    |
| `qd.p() & qd.v()`      | `color : str (from colors in termcolor) ` |
| `qd.p()`               | `msg : str`                               |
| `qd.v()`               | `inline : bool`                           |
| `qd.track() & qd.rt()` | `autoclear : bool`                        |

| Kwarg    | Possible Values                                                                                    |
| -------- | -------------------------------------------------------------------------------------------------- |
| `status` | `"OFF", "O", "ERROR", "ERR", "E", "WARNING", "WARN", "W", "DEBUG", "D", "INFO", "I", "TRACE", "T"` |
| `color`  | `"grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"`                             |
