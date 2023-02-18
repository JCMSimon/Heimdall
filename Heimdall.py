import os
from datetime import datetime as dt
from json import JSONDecodeError
from json import load as jsonload
from multiprocessing import Process
from sys import argv
from typing import Literal

from plugins._PluginRegister import PluginRegister
from src.Core import Core
from src.gui import GUI
from src.Loader import LoadingUI
from src.Logger import Logger
from src.SetupUI import Setup

def GuiStart(debug) -> Literal[1, 0]:
	"""
	It starts the GUI and the core

	Args:
	  debug: Boolean, if true, the program will run in debug mode

	Returns:
	  The return value is the exit code of the program.
	"""
	logger = Logger("Heimdal // Main",debug=debug)
	if "--openSettings" in argv[1:] and "--forceUpdate" in argv[1:]:
		logger.errorMsg("The Arguments '--openSetting' and '--forceUpdate' cannot be used at the same time.")
		return 1
	logger.debugMsg("Checking for update config")
	if CheckUpdateConfig():
		logger.debugMsg("Update config found")
	else:
		logger.debugMsg("Update config not found, created one")
	checkForUpdate(logger,debug)
	#############
	logger.debugMsg("Starting Loading UI")
	loadingUIProcess = startLoadingUI(debug)
	logger.debugMsg("Loading Plugins")
	pluginRegister,pluginNames = loadPlugins(debug)
	logger.debugMsg("Closing Loading UI")
	loadingUIProcess.terminate()
	logger.debugMsg("Starting Main User Interface")
	mainGUI = GUI(pluginNames,debug=debug)
	nodeEditor = mainGUI.returnEditor()
	logger.debugMsg("Starting Heimdall Core")
	core = Core(pluginRegister,nodeEditor,debug)
	if not CheckOneTimeSetupDone(logger) or "--openSettings" in argv[1:]:
		setupProcess = Process(target=oneTimeSetup,args=[logger,debug],daemon=True)
		setupProcess.start()
		setupProcess.join()
	mainGUI.start(core)
	return 0

def CheckUpdateConfig() -> bool:
	"""
	If the directories "saves" and "pluginData" don't exist, create them. If the file
	"updateconfig.json" doesn't exist, create it.

	Returns:
	  A boolean value (Success or not).
	"""
	if not os.path.isdir("saves"):
		os.system("mkdir saves")
	if not os.path.isdir("pluginData"):
		os.system("mkdir pluginData")
	if not os.path.isfile("updateconfig.json"):
		with open("updateconfig.json","w") as file:
			time = dt.now().replace(microsecond=0).isoformat()
			file.write(f"{{\n\t\"lastUpdated\": \"{time}\",\n\t\"ignoreMinorUpdates\": false,\n\t\"ignoreMajorUpdates\": false,\n\t\"ignorePreRequestWarnings\": false,\n\t\"autoUpdate\": false,\n\t\"oneTimeSetupDone\": false,\n\t\"autoUpdatePlugins\": false\n}}")
			return False
	return True

def checkForUpdate(logger,debug) -> None:
	"""
	It checks if the user has enabled auto-updates in the settings, and if so, it runs the update
	program

	Args:
	  logger: A logger object
	  debug: Boolean
	"""
	with open("updateconfig.json","r") as file:
		if (
			jsonload(file)["autoUpdate"]
			and "--openSettings" not in argv[1:]
			or "--forceUpdate" in argv[1:]
		):
			logger.debugMsg("Checking for Updates (Autoupdate enabled)")
			arg = " --debug" if debug else ""
			os.system(f"HeimdallUpdate.exe{arg}")

def startLoader(debug) -> None:
	"""
	It creates a new instance of the LoadingUI

	Args:
	  debug: Boolean
	"""
	_ = LoadingUI(debug=debug)

def loadPlugins(debug) -> tuple[PluginRegister,list]:
	"""
	It returns a tuple of a PluginRegister object and a list of plugin names

	Args:
	  debug: Boolean, whether to print debug messages or not

	Returns:
	  A tuple of two items. The first item is a PluginRegister object. The second item is a list of
	strings.
	"""
	pluginRegister = PluginRegister(debug)
	return pluginRegister,pluginRegister.getPluginNames()

def startLoadingUI(debug) -> Process:
	"""
	It starts a process that runs the startLoader function.

	Args:
	  debug: Boolean

	Returns:
	  A Process object.
	"""
	loadingUIProcess = Process(target=startLoader,args=[debug],daemon=True)
	loadingUIProcess.start()
	return loadingUIProcess

def CheckOneTimeSetupDone(logger) -> bool | None:
	"""
	It checks if the one time setup has been done.

	Args:
	  logger: The logger object

	Returns:
	  The return value is a boolean value.
	"""
	try:
		with open("updateconfig.json","r") as file:
			return jsonload(file)["oneTimeSetupDone"]
	except JSONDecodeError:
		logger.infoMsg("updateconfig.json corrupted or missing.")
		os.system("del updateconfig.json")
		if not CheckUpdateConfig():
			logger.infoMsg("Success")
		else:
			logger.infoMsg("This should not be shown at any time :)")

def oneTimeSetup(logger,debug) -> None:
	"""
	This function is called once at the beginning of the script. It creates a Setup object which is used to ask the User for Settings and calls its
	constructor

	Args:
	  logger: This is the logger object that you created in the main function.
	  debug: True or False
	"""
	logger.debugMsg("Starting One Time Setup")
	_ = Setup(debug=debug)

if __name__ == "__main__":
	GuiStart("--debug" in argv[1:])