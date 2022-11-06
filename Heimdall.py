import multiprocessing
import sys

from src.Logger import Logger
from src.Loader import Loader
from plugins._PluginRegister import PluginRegister
from src.Core import Core
from src.Gui import GUI

def start(debug):
	logger = Logger("Start-up",debug=debug)
	logger.debugMsg("Starting Loading Graphic")
	loaderProcess = multiprocessing.Process(target=startLoader,args=[debug,logger])
	loaderProcess.start()
	logger.debugMsg("Loading Plugins")
	pluginRegister = PluginRegister(debug)
	pluginNames = pluginRegister.getPluginNames()
	logger.debugMsg("Closing Loading Graphic")
	loaderProcess.terminate()
	logger.debugMsg("Starting Main User Interface")
	#
	gui = GUI(pluginNames,debug=debug)
	nodeEditor = gui.returnEditor()
	core = Core(pluginRegister,nodeEditor,debug=debug)
	gui.start(core)


def startLoader(debug,logger):
	_ = Loader(debug=debug)

if __name__ == "__main__":
	if "--debug" in sys.argv[1:]:
		debug=True
	else:
		debug=False
	start(debug)
