from json import load
from lib.loader import Loader
from lib.gui import GUI
import multiprocessing
import time

def start():
	loaderProcess = multiprocessing.Process(target=startLoader)
	loaderProcess.start()
	time.sleep(3)
	loaderProcess.terminate()
	print("i still work")
	# init start ui
	# init pluginregister
	# init gui and pass register
	# MainInterface = GUI()

def startLoader():
	load = Loader()



if __name__ == "__main__":
	start()