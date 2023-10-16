from deltalogging.logger import Logger
from pystyle import Colors

Logger.info("Logger: Info")
Logger.warning("Logger: Warning")
Logger.error("Logger: Error")
print("")

colors = ["red", "green", "blue", "white", "gray", "yellow", "purple", "cyan", "orange", "pink", "turquoise", "light_gray", "dark_gray", "light_red", "light_green", "light_blue", "dark_red", "dark_green", "dark_blue"]

for color in colors:
    colorname = getattr(Colors, color)
    print(colorname + "Logger: Print, Color: " + color)


