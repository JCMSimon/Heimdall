import os
from datetime import datetime as dt
from json import JSONDecodeError
from json import load as jsonload
from multiprocessing import Process
from sys import argv

from plugins._PluginRegister import PluginRegister
from src.Core import Core
from src.gui import GUI
from src.Loader import LoadingUI
from src.Logger import Logger
from src.SetupUI import Setup

def fullStart(debug) -> None:
	"""
	It starts the program with the full GUI

	Args:
	  debug: Boolean
	"""
	logger = startLogger("Heimdall/Main",debug)
	# Check compatibillity
	if "--openSettings" in argv[1:] and "--forceUpdate" in argv[1:]:
		logger.errorMsg("Cant have force update and open settings together")
		return
	# Check updateconfig.json
	logger.debugMsg("Checking for update config")
	if CheckUpdateConfig():
		logger.debugMsg("Update config found")
	else:
		logger.debugMsg("Update config not found, created one")
	# Start update Process
	checkForUpdate(logger,debug)
	# Start LoadingUI
	logger.debugMsg("Starting Loading UI")
	loadingUIProcess = startLoadingUI(debug)
	# Load Plugins
	logger.debugMsg("Loading Plugins")
	pluginRegister,pluginNames = loadPlugins(debug)
	# Close Loding UI
	logger.debugMsg("Closing Loading UI")
	loadingUIProcess.terminate()
	# Start Main GUI
	logger.debugMsg("Starting Main User Interface")
	mainGUI = GUI(pluginNames,debug=debug)
	# Get refernce to the node editor
	nodeEditor = mainGUI.returnEditor()
	logger.debugMsg("Starting Heimdall Core")
	core = Core(pluginRegister,nodeEditor,debug)
	# Start One time setup if needed
	if not CheckOneTimeSetupDone(logger) or bool("--openSettings" in argv[1:]):
		setupProcess = Process(target=oneTimeSetup,args=[logger,debug],daemon=True)
		setupProcess.start()
		setupProcess.join()
	mainGUI.start(core)

def startLogger(prefix,debug) -> Logger:
	"""
	It returns a Logger object with the given prefix and debug flag

	Args:
	  prefix: This is the prefix of the log messages.
	  debug: True/False

	Returns:
	  A Logger object
	"""
	return Logger(prefix,debug=debug)

def CheckUpdateConfig() -> bool:
	"""
	If the updateconfig.json file doesn't exist, create it and return false. If it does exist, return true

	Returns:
	  a boolean value.
	"""
	if not os.path.isdir("saves"):
		os.system("mkdir saves")
	if not os.path.isfile("updateconfig.json"):
		with open("updateconfig.json","w") as file:
			time = dt.now().replace(microsecond=0).isoformat()
			file.write(f"{{\n\t\"lastUpdated\": \"{time}\",\n\t\"ignoreMinorUpdates\": false,\n\t\"ignoreMajorUpdates\": false,\n\t\"ignorePreRequestWarnings\": false,\n\t\"autoUpdate\": false,\n\t\"oneTimeSetupDone\": false,\n\t\"autoUpdatePlugins\": false\n}}")
			return False
	return True

def checkForUpdate(logger,debug) -> None:
	"""
	It checks if the user has enabled auto-updates, and if so, it runs the update program.

	Args:
	  logger: A logger object
	  debug: True/False
	"""
	with open("updateconfig.json","r") as file:
		if jsonload(file)["autoUpdate"] and not "--openSettings" in argv[1:] or "--forceUpdate" in argv[1:]:
			logger.debugMsg("Checking for Updates (Autoupdate enabled)")
			arg = ""
			if debug:
				arg = " --debug"
			os.system(f"HeimdallUpdate.exe{arg}")

def startLoader(debug) -> None:
	"""
	It creates a new instance of the Loader class, and passes the debug argument to the class

	Args:
	  debug: True/False
	"""
	_ = LoadingUI(debug=debug)

def loadPlugins(debug) -> tuple[PluginRegister,list]:
	"""
	It creates a PluginRegister object, and then returns the object and a list of the names of the
	plugins that were loaded

	Args:
	  debug: Boolean, if True, will print debug messages

	Returns:
	  A tuple of two items. The first item is the pluginRegister object. The second item is a list of
	plugin names.
	"""
	pluginRegister = PluginRegister(debug)
	return pluginRegister,pluginRegister.getPluginNames()

def startLoadingUI(debug) -> Process:
	"""
	It starts a new process that runs the loading UI.

	Args:
	  debug: True/False

	Returns:
	  The process object.
	"""
	loadingUIProcess = Process(target=startLoader,args=[debug],daemon=True)
	loadingUIProcess.start()
	return loadingUIProcess

def CheckOneTimeSetupDone(logger) -> bool:
	"""
	It checks if the one time setup has been done

	Args:
	  logger: A logger object

	Returns:
	  The return value of the function is the value of the key "oneTimeSetupDone" in the json file.
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
			logger.infoMsg("This should not be shown at any time :")

def oneTimeSetup(logger,debug) -> None:
	"""
	This function is called once at the beginning of the script. It lets the user adjust Settings

	Args:
	  logger: This is the logger object that you created in the main function.
	  debug: True/False
	"""
	logger.debugMsg("Starting One Time Setup")
	_ = Setup(debug=debug)

if __name__ == "__main__":
	fullStart(bool("--debug" in argv[1:]))