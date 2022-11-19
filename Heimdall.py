from multiprocessing import Process
from sys import argv
import os

from src.Logger import Logger
#from src.Loader import Loader
from src.Core import Core
from src.gui import GUI
from plugins._PluginRegister import PluginRegister

def defaultStart(debug):
	logger = Logger("Start-up",debug=debug)
	logger.debugMsg("Starting Loading Graphic")
	loaderProcess = Process(target=startLoader,args=[debug])
	loaderProcess.start()
	logger.debugMsg("Checking for update config")
	result = CheckUpdateConfig()
	if result:
		logger.debugMsg("Update config found")
	else:
		logger.debugMsg("Update config not found, created one")
	logger.debugMsg("Loading API Keys")
	logger.debugMsg("Loading Plugins")
	pluginRegister = PluginRegister(debug)
	pluginNames = pluginRegister.getPluginNames()
	logger.debugMsg("Closing Loading Graphic")
	loaderProcess.terminate()
	logger.debugMsg("Starting Main User Interface")
	gui = GUI(pluginNames,debug=debug)
	nodeEditor = gui.returnEditor()
	core = Core(pluginRegister,nodeEditor,debug=debug)
	gui.start(core)

def startLoader(debug):
	_ = Loader(debug=debug)

def CheckUpdateConfig():
	if not os.path.isfile("updateconfig.json"):
		with open("updateconfig.json","w") as f:
			f.write("{\n\t\"lastUpdated\": \"2020-08-01T00:00:00\",\n\t\"ignoreMinorUpdates\": false,\n\t\"ignoreMajorUpdates\": false\n}")
			return False
	return True

if __name__ == "__main__":
	debug = bool("--debug" in argv[1:])
	defaultStart(debug)
