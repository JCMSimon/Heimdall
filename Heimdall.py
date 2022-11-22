from multiprocessing import Process
from sys import argv
from json import JSONDecodeError, load as jsonload
import os
from datetime import datetime

from src.Logger import Logger
from src.Loader import Loader
from src.Core import Core
from src.SetupUI import Setup
from src.gui import GUI
from plugins._PluginRegister import PluginRegister

def defaultStart(debug):
	logger = Logger("Start-up",debug=debug)
	checkForUpdate(logger,debug)
	logger.debugMsg("Starting Loading Graphic")
	loaderProcess = Process(target=startLoader,args=[debug],daemon=True)
	loaderProcess.start()
	logger.debugMsg("Checking for update config")
	if CheckUpdateConfig():
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
	if not CheckSetupDone(logger):
		setupProcess = Process(target=oneTimeSetup,args=[logger,debug],daemon=True)
		setupProcess.start()
		setupProcess.join()
	gui.start(core)

def startLoader(debug):
	_ = Loader(debug=debug)

def checkForUpdate(logger,debug):
	logger.debugMsg("Checking for Updates")
	try:
		with open("updateconfig.json","r") as file:
			if jsonload(file)["autoUpdate"]:
				if debug:
					os.system(f"HeimdallUpdate.exe --debug")
				else:
					os.system(f"HeimdallUpdate.exe")
	except (JSONDecodeError,FileNotFoundError):
		logger.infoMsg("updateconfig corrupted. Resetting to defaults")
		os.system("del updateconfig.json")
		if not CheckUpdateConfig():
			logger.infoMsg("Success")


def oneTimeSetup(logger,debug):
	logger.debugMsg("Starting One Time Setup")
	_ = Setup(debug=debug)

def CheckUpdateConfig():
	if not os.path.isfile("updateconfig.json"):
		with open("updateconfig.json","w") as f:
			time = datetime.now().replace(microsecond=0).isoformat()
			f.write(f"{{\n\t\"lastUpdated\": \"{time}\",\n\t\"ignoreMinorUpdates\": false,\n\t\"ignoreMajorUpdates\": false,\n\t\"ignorePreRequestWarnings\": false,\n\t\"autoUpdate\": false,\n\t\"oneTimeSetupDone\": false\n}}")
			return False
	return True

def CheckSetupDone(logger):
	try:
		with open("updateconfig.json","r") as file:
			return jsonload(file)["oneTimeSetupDone"]
	except JSONDecodeError:
		logger.infoMsg("updateconfig corrupted. Resetting to defaults")
		os.system("del updateconfig.json")
		if not CheckUpdateConfig():
			logger.infoMsg("Success")

if __name__ == "__main__":
	debug = bool("--debug" in argv[1:])
	defaultStart(debug)
