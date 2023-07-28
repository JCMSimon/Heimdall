from src.gui.Main import GUI
from sys import argv

if "--debug" in argv:
    DEBUG = True
else:
    DEBUG = False


t = GUI(DEBUG=DEBUG)
# t.start()

# TODO
