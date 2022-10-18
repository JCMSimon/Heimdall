from src.loader import Loader
from src.gui import GUI
from src._Logger import Logger
import multiprocessing
from plugins._PluginRegister import PluginRegister

def start(debug):
	# loaderProcess = multiprocessing.Process(target=startLoader,args=[debug])
	# loaderProcess.start()

	plreg = PluginRegister(debug)
	plugins = plreg.getPluginNames()
	print(plugins)
	plreg.runPlugin(plugins[0],"Simon")
	# pl reg here
		# get all files in plugin folder
		# make a dict of the file.getDisplayName and a reference to the plugin class.

		# Example
		# Plugin Name: Username.py
		# *get file name*

		# import Username
		# PluginCallReference = Username.Username(debug)

		# return the dict

	# time.sleep(3)
	# loaderProcess.terminate()
	mainGui = GUI("PluginRegisterPlaceholder",debug=debug)

def startLoader(debug):
	load = Loader(debug=debug)

if __name__ == "__main__":
	debug = True # fully implemented. get later as cli argument // startup argument
	start(debug)