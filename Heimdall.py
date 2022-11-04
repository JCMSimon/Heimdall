import multiprocessing
import sys

from plugins._PluginRegister import PluginRegister
from src._Logger import Logger
from src.gui import GUI
from src.loader import Loader

def start(debug):
	logger = Logger("Start-up",debug=debug)
	logger.debugMsg("Starting Loading Graphic")
	loaderProcess = multiprocessing.Process(target=startLoader,args=[debug,logger])
	loaderProcess.start()
	logger.debugMsg("Loading Plugins")
	pluginRegister = PluginRegister(debug)
	logger.debugMsg("Closing Loading Graphic")
	loaderProcess.terminate()
	logger.debugMsg("Starting Main User Interface")
	mainGui = GUI(pluginRegister,debug=debug)

def startLoader(debug,logger):
	_ = Loader(debug=debug)

if __name__ == "__main__":
	if "--debug" in sys.argv[1:]:
		debug=True
	else:
		debug=False
	start(debug)
