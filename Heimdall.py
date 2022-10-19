import multiprocessing

from plugins._PluginRegister import PluginRegister
from src._Logger import Logger
from src.gui import GUI
from src.loader import Loader

def start(debug):
	logger = Logger("Start-up",debug=debug)
	# loaderProcess = multiprocessing.Process(target=startLoader,args=[debug,logger])
	# loaderProcess.start()
	# logger.debugMsg("Loading Plugins")
	pluginRegister = PluginRegister(debug)
	# logger.debugMsg("Closing Loading Graphic")
	# loaderProcess.terminate()
	logger.debugMsg("Startin Main User Interface")
	mainGui = GUI(pluginRegister,debug=debug)

def startLoader(debug,logger):
	logger.debugMsg("Starting Loading Graphic")
	_ = Loader(debug=debug)

if __name__ == "__main__":
	debug = True # fully implemented. get later as cli argument // startup argument
	start(debug)