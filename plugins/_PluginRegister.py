from os import walk
from src.Logger import Logger
from json import load as jsonload
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
		self.pluginsUpdated = False
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)
		self.plugins = self.loadPlugins()

	def getPluginNames(self):
		"""
		If there are no plugins, exit

		Returns:
		  A list of the names of the plugins that are working.
		"""
		if not self.plugins.keys():
			self.logger.errorMsg("No working Plugins. Shutting down.")
			exit(0)
		return [name for name in self.plugins.keys() if self.plugins[name]["display"]]

	def getPluginNamesByType(self,datatype):
		"""
		It returns a list of plugin names that accept the given datatype

		Args:
		  datatype: The type of data that the plugin accepts.

		Returns:
		  A list of plugin names that accept the given datatype.
		"""
		return [name for name in self.plugins.keys() if datatype in self.plugins[name]["accepts"]]

	def reload(self):
		"""
		It reloads the plugins
		"""
		self.logger.infoMsg("Reloading Plugins")
		self.plugins = self.loadPlugins()

	def loadPlugins(self) -> dict:
		"""
		It loads all the plugins in the plugins folder and returns a dictionary of the plugins with their
		display name, version, accepts, and display function.

		Returns:
			A dictionary of dictionaries.
		"""
		# sourcery skip: move-assign-in-block, use-named-expression
		for (_, _, filenames) in walk("./plugins"):
			files = [filename for filename in filenames if not filename.startswith("_")]
			break
		plugins = {}
		updatedPlugins = []
		for plugin in files:
			plugin = plugin.replace(".py","")
			if pluginClassInstance := self.getPluginInstance(plugin):
				plugins[plugin] = {
					"displayName":pluginClassInstance.getDisplayName(),
					"version":pluginClassInstance.getVersion(),
					"accepts":pluginClassInstance.accepts(),
					"display":pluginClassInstance.display,
				}
				self.logger.infoMsg(f"{pluginClassInstance.getDisplayName()} v{pluginClassInstance.getVersion()} loaded succesfully!")
		if updatedPlugins:
			self.logger.infoMsg(f"While loading the following plugins were Updated: {', '.join(updatedPlugins)}. A restart is suggested.")
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

	def getPluginInstance(self,pluginName) -> None:
		"""
		It imports a module from the plugins folder, then returns an instance of the class with the same
		name as the module

		Args:
		  pluginName: The name of the plugin to load.

		Returns:
		  The plugin class instance.
		"""
		try:
			pluginModule = __import__(f'plugins.{pluginName}', fromlist=[f'{pluginName}'])
			pluginClass = getattr(pluginModule, f'{pluginName}')
			return pluginClass(debug=self.debug)
		except (AttributeError,TypeError):
			self.logger.errorMsg(f"{pluginName} could not be loaded!")
			return