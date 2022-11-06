from multiprocessing import Process
from sys import argv

from src.Logger import Logger
from src.Loader import Loader
from src.Core import Core
from src.Gui import GUI
from plugins._PluginRegister import PluginRegister

def defaultStart(debug):
	logger = Logger("Start-up",debug=debug)
	logger.debugMsg("Starting Loading Graphic")
	loaderProcess = Process(target=startLoader,args=[debug]).start()
	logger.debugMsg("Loading Plugins")
	pluginRegister = PluginRegister(debug)
	pluginNames = pluginRegister.getPluginNames()
	logger.debugMsg("Closing Loading Graphic")
	loaderProcess.terminate()
	loaderProcess.close()
	logger.debugMsg("Starting Main User Interface")
	gui = GUI(pluginNames,debug=debug)
	nodeEditor = gui.returnEditor()
	core = Core(pluginRegister,nodeEditor,debug=debug)
	gui.start(core)

def startLoader(debug):
	_ = Loader(debug=debug)

if __name__ == "__main__":
	if "--debug" in argv[1:]:
		debug=True
	else:
		debug=False
	defaultStart(debug)