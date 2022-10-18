import importlib
from src._Logger import Logger
from os import walk

class PluginRegister():
	def __init__(self,debug=False) -> None:
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)
		self.plugins = self.getFiles()

	def reload(self):
		self.getFiles()

	# How to import Plugin
	# test = importlib.__import__("plugins.Username")
	# test2 = test.Username.Username(debug=True)
	# test2.run()

	def getFiles(self):
		fileNames = []
		for (_, _, filename) in walk("./plugins"):
				fileNames.extend(filename)
				break
		for file in fileNames:
			if str(file).startswith("_"):
				fileNames.remove(file)
		for file in fileNames:
			temp = str(file).replace(".py","")
			fileNames.remove(file)
			fileNames.append(temp)
		return fileNames

	def getPluginNames(self):
		return self.plugins

	def runPlugin(self,pluginName,arg):
		self.logger.infoMsg(f"Running Plugin '{pluginName}' with Argument '{arg}'")
		pass #idk smth smth importlib smth smth run smth smth get node list as return smth smth process further in gui

