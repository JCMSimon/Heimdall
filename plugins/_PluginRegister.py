from os import walk

from src.Logger import Logger

class PluginRegister():
	def __init__(self,debug=False) -> None:
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)
		self.plugins = self.getFiles()

	def reload(self):
		self.logger.debugMsg("Reloading Plugins")
		self.getFiles()

	def getFiles(self):
		#This Method is prob the worst of all. def gotta rework this
		fileNames = []
		self.logger.debugMsg("Files in Plugin Folder:")
		for (_, _, filename) in walk("./plugins"):
				self.logger.debugMsg(f"- {filename}")
				fileNames.extend(filename)
				break
		self.logger.debugMsg("Removing Files:")
		for name in fileNames:
			if str(name).startswith("_"):
				self.logger.debugMsg(f"- {name}")
				fileNames.remove(name)
		finalNames = []
		for name in fileNames:
			finalNames.append(str(name).replace(".py",""))
		self.logger.debugMsg(f"Final List: {finalNames}")
		return finalNames


	def getPluginNames(self):
		return self.plugins

	def runPlugin(self,pluginName,arg) -> list:
		self.logger.debugMsg(f"Running Plugin '{pluginName}' with Argument '{arg}'")
		plugin = __import__(f'plugins.{pluginName}', fromlist=[f'{pluginName}'])
		pluginClass = getattr(plugin, f'{pluginName}')
		try:
			pluginClassInstance = pluginClass(debug=self.debug)
		except TypeError:
			self.logger.errorMsg(f"Plugin {pluginName} is not working.")
			return
		data = pluginClassInstance.run(arg)
		return data

if __name__ == "__main__":
	test = PluginRegister(debug=True)