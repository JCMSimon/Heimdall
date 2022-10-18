import importlib
from os import walk

from src._Logger import Logger

class PluginRegister():
	def __init__(self,debug=False) -> None:
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)
		self.plugins = self.getFiles()

	def reload(self):
		self.logger.debugMsg("Reloading Plugins")
		self.getFiles()

	def getFiles(self):
		fileNames = []
		for (_, _, filename) in walk("./plugins"):
				fileNames.extend(filename)
				break
		self.logger.debugMsg(f"Files in Plugin Folder:")
		for file in fileNames:
			self.logger.debugMsg(f"-{file}")
			if str(file).startswith("_"):
				fileNames.remove(file)
		self.logger.debugMsg(f"Plugins in Plugin Folder:")
		for file in fileNames:
			temp = str(file).replace(".py","")
			fileNames.remove(file)
			fileNames.append(temp)
			self.logger.debugMsg(f"-{temp}")
		return fileNames

	def getPluginNames(self):
		return self.plugins

	def runPlugin(self,pluginName,arg) -> list:
		self.logger.debugMsg(f"Running Plugin '{pluginName}' with Argument '{arg}'")
		pluginFile = importlib.__import__(f"plugins.{pluginName}")
		# get classes from pluginfile
		# test if plugin name matches plugin class
		pass