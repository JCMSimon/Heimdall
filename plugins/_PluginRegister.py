from os import walk
from src.Logger import Logger
from plugins.lib import Plugin
class PluginRegister():
	"""
	Plugin Register/Manager for Heimdall
	"""
	def __init__(self,DEBUG=False) -> None:
		"""
		Initialises a PLuginRegister Instance

		Args:
		  DEBUG: If set to True, the logger will print debug information to the console. Defaults to False
		"""
		self._DEBUG = DEBUG
		self.logger = Logger("PluginRegister",DEBUG=self._DEBUG)
		self.plugins = self.loadPlugins()

	def loadPlugins(self) -> dict:
		"""
		It loads all the plugins in the plugins folder and returns a dictionary of the plugins

		Returns:
		  A dictionary of Plugins and their data.
		"""
		plugins = {}
		for pluginName in self.getPluginFiles():
			if pluginClassInstance := self.getPluginInstance(pluginName):
				plugins[pluginName] = {
					"displayName":pluginClassInstance.displayname(),
					"version":pluginClassInstance.version(),
					"accepts":pluginClassInstance.accepts(),
					"defaultInput":pluginClassInstance.defaultInput(),
					"display":pluginClassInstance.display,
					"runMethod":pluginClassInstance.run,
				}
				self.logger.infoMsg(f"{plugins[pluginName]['displayName']} v{plugins[pluginName]['version']} loaded succesfully!")
		return plugins

	def getPluginFiles(self) -> list[str]:
		"""
		It returns a list of all the files in the plugins directory that don't start with an underscore

		Returns:
		  A list of strings.
		"""
		for (_, _, filenames) in walk("./plugins"):
			files = [filename.replace(".py","") for filename in filenames if not filename.startswith("_")]
			break
		return files

	def getPluginInstance(self,pluginName) -> Plugin:
		"""
		It imports the plugin file and creates a class instance of the plugin

		Args:
		  pluginName: The name of the plugin to load.

		Returns:
		  A Plugin instance
		"""
		try:
			# Import the Plugin File
			pluginModule = __import__(f'plugins.{pluginName}', fromlist=[pluginName])
			# Create a Class instance of the Plugin
			pluginClass = getattr(pluginModule, pluginName)
			return pluginClass(DEBUG=self._DEBUG)
		except AttributeError as e:
			self.logger.errorMsg(f"{pluginName} could not be loaded! ({e})")
			return None

	def reload(self) -> None:
		"""
		It reloads the plugins
		"""
		self.logger.infoMsg("Reloading Plugins")
		self.plugins = self.loadPlugins()

	def runPlugin(self,pluginName,keyword) -> list:
		"""
		It takes a plugin name and a keyword, and returns a list of results from the plugin

		Args:
		  pluginName: The name of the plugin to run.
		  keyword: The keyword that the user entered

		Returns:
		  A list of dictionaries.
		"""
		self.logger.debugMsg(f"Running Plugin '{pluginName}' with Argument '{keyword}'")
		return self.getPluginInstance(pluginName).run(keyword)

	def getDefaultDatapointByName(self,pluginName) -> str:
		"""
		> This function returns the default datapoint for a given plugin

		Args:
		  pluginName: The name of the plugin you want to get the default datapoint from.

		Returns:
		  The default datapoint for the plugin.
		"""
		return self.plugins[pluginName]["defaultInput"]

	def getPluginNamesByDatapoint(self,DATAPOINT) -> list:
		"""
		> Return a list of plugin names that have a default input of the given datapoint

		Args:
		  DATAPOINT: The datapoint that you want to get the plugins for.

		Returns:
		  A list of plugin names that have a defaultInput of DATAPOINT.
		"""
		return [pluginName for pluginName in self.plugins.keys() if self.plugins[pluginName]["defaultInput"] == DATAPOINT]