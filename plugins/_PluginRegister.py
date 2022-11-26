from os import walk

from src.Logger import Logger


class PluginRegister():
	"""
	Plugin Register for Heimdall
	"""
	def __init__(self,debug=False):
		"""
		Loads Plugins

		Args:
		  debug: If set to True, the logger will print out debug messages. Defaults to False
		"""
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)
		self.plugins = self.getFiles()

	def reload(self):
		"""
		It reloads the plugins
		"""
		self.logger.debugMsg("Reloading Plugins")
		self.getFiles()

	def getFiles(self):
		"""
		It gets all the files in the plugins folder, removes the ones that start with an underscore, and
		returns the list of files

		Returns:
		  A list of all the files in the plugins folder that are not starting with an underscore.
		"""
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

	def getPluginNamesByType(self,datatype):
		"""
		It returns a list of plugins that accept the given datatype

		Args:
		  datatype: The type of data that the plugin accepts.

		Returns:
		  A list of plugin names.
		"""
		list = []
		for pluginName in self.plugins:
			plugin = __import__(f'plugins.{pluginName}', fromlist=[f'{pluginName}'])
			pluginClass = getattr(plugin, f'{pluginName}')
			try:
				pluginClassInstance = pluginClass(debug=self.debug)
			except TypeError:
				self.logger.errorMsg(f"Plugin {pluginName} is not working.")
				return
			else:
				if datatype in pluginClassInstance.accepts():
					list.append(pluginName)
			self.logger.debugMsg(f"Found {len(list)} compatible Plugins")
		return list

	def getPluginNames(self):
		"""
		It returns a list of all the plugins that are currently loaded

		Returns:
		  The list of plugins.
		"""
		return self.plugins

	def runPlugin(self,pluginName,arg) -> list:
		"""
		It imports a plugin, creates an instance of the plugin, and then runs the plugin

		Args:
		  pluginName: The name of the plugin to run.
		  arg: The argument that the user has given to the plugin.

		Returns:
		  A list of dictionaries.
		"""
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