import importlib
from src._Logger import Logger

class PluginRegister():
	def __init__(self,debug=False) -> None:
		self.debug = debug
		self.logger = Logger("PluginRegister",debug=self.debug)

