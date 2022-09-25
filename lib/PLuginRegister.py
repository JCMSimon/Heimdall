import importlib
from lib.Logger import Logger

class PluginRegister():
	def __init__(self,debug) -> None:
		self.logger = Logger("PluginRegister")
		plugins = self.loadAllPlugins()

	def loadAllPlugins(self):
		class1 = getattr(importlib.import_module("plugins.plugins.ex"), "tset")
		class1.test()
	def runPlugin(pluginName,*kwargs):
		pass

 #why is it PLugin and not Plugin? I don't know, I'm not a native english speaker and I don't know how to spell it correctly :D Wow ok then copilot