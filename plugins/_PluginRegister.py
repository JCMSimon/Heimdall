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
		self.plugins = self.loadPlugins()

	def getPluginNames(self):
		return [name for name in self.plugins.keys() if self.plugins[name]["display"]]

	def getPluginNamesByType(self,datatype):
		return [name for name in self.plugins.keys() if datatype in self.plugins[name]["accepts"]]

	def reload(self):
		"""
		It reloads the plugins
		"""
		self.logger.debugMsg("Reloading Plugins")
		self.loadPlugins()

	def loadPlugins(self):
		for (_, _, filenames) in walk("./plugins"):
			files = [filename for filename in filenames if not filename.startswith("_")]
			break
		plugins = {}
		for plugin in files:
			plugin = plugin.replace(".py","")
			pluginClassInstance = self.getPluginInstance(plugin)
			plugins[plugin] = {
				"displayName":pluginClassInstance.getDisplayName(),
				"version":pluginClassInstance.getVersion(),
				"accepts":pluginClassInstance.accepts(),
				"display":pluginClassInstance.display,
			}
		return plugins

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
		return self.getPluginInstance(pluginName).run(arg)

	def getPluginInstance(self,pluginName):
		pluginModule = __import__(f'plugins.{pluginName}', fromlist=[f'{pluginName}'])
		pluginClass = getattr(pluginModule, f'{pluginName}')
		try:
			return pluginClass(debug=self.debug)
		except TypeError:
			self.logger.errorMsg(f"Plugin {pluginName} is not working.")
			return