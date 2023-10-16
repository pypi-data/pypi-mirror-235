# DeltaLogging

##  Installation
You can install PyLogger using pip:
```bash
pip install  DeltaLogging
```
## Usage
Logging:
```python
from deltalogging import Logger

Logger.info("Info")
Logger.error("Error")
Logger.warning("Warning")

#You need to import pystyle to use logger.print
from pystyle import Colors
#Now you need a color, like Colors.Cyan
color = Colors.Cyan
Logger.print(color + "Print")
```
Utilities:
```python
from deltalogging import Logger
Logger.cls() # Clear console
Logger.title(title) # Set console title
Logger.cmd(cmd) # Execute a command
```
## Compatibility
You can use deltalogging on both Windows and Linux.

## Message from author
Contributions are welcome! Feel free to submit issues and pr's! github.com/toxinsfx/deltalogging

Enjoy using DeltaLogging!







