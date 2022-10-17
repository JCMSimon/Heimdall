from json import load
from src.loader import Loader
from src.gui import GUI
from src._Logger import Logger
import multiprocessing
import time

def start(debug):
	loaderProcess = multiprocessing.Process(target=startLoader,args=[debug])
	loaderProcess.start()
	time.sleep(3)
	loaderProcess.terminate()
	mainGui = GUI("PluginRegisterPlaceholder",debug=debug)

def startLoader(debug):
	load = Loader(debug=debug)

if __name__ == "__main__":
	debug = False
	start(debug)