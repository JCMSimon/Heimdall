import multiprocessing
import sys

from plugins._PluginRegister import PluginRegister
from src._Logger import Logger
from src.Gui import GUI
from src.Loader import Loader
from src.Core import Core

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
	# unsure if gui itself is properly returned
	gui = GUI(pluginRegister,debug=debug)
	nodeEditor = gui.returnEditor()
	core = Core(pluginRegister,nodeEditor,debug=debug)
	gui.start(debug,core)


def startLoader(debug,logger):
	_ = Loader(debug=debug)

if __name__ == "__main__":
	if "--debug" in sys.argv[1:]:
		debug=True
	else:
		debug=False
	start(debug)
