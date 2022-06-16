# Welcome to simpleDebug!

## :warning: Yet to be deployed, please wait 1 - 2 days

simpleDebug offers a standardized alternative to `print("here")` and `print(my_var)`, with simple, quick, and efficient logging functions that provide information without the need to repeat yourself. Generally, the best use case is for small scale applications or test code, where a complete debugger is overkill, but `print("here")` can get overly tedious to repeadly type. Function names are purposefully shortened avoid writing out long function calls.

## Installation

`>> pip install simpleDebug`

## Quick Start

#### Initialization

To use the package, you need to create an instance of `simpleDebug`, from which methods can be called.

```python
import simpleDebug
sd = simpleDebug()
```

#### Basic Logging

The two essential functions for logging are `sd.p()` and `sd.v()`.

```python
# Logs index, line number, timestamp, and a optional message
sd.p()

#Logs all variables with thier current values
sd.v()
```

#### AutoVar Configs

AutoVar configs allow you to set up a list of varibles with a certain format to be printed with current values with the `sd.vc()` function, and then allows you to access that printing configuration with `sd.v(config_key)`.

```python
a = 1
b = 2
# Create a config that prints the variables a and b, where the config_key is 1
sd.vc(1, "a", "b")

# Would print just a & b
sd.v(1) # config_key is the first argument
```

#### Variable Tracking

`simpleDebug` also provides lightweight, real-time variable tracking in the terminal through `sd.track()` and `sd.rt()`

```python
a = 1

# Would print the value of a every 10ms for 5s
sd.track("a", 10, 5)

# Preset Function for indefinite real-time tracking
sd.rt("a")
```

For more details, read the full documentation on [PyPI](https://pypi.org/).
