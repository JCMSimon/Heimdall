import toml

from src.Logger import Logger


class APIRegister:
	"""Utility for plugins to request api keys from the config.toml file"""
	def __init__(self, apiKeys=None, DEBUG=False) -> None:
		"""
		It takes a list of keys, and if the list is not empty, it loads the config file

		Args:
		  apiKeys: A list of strings that are the names of the keys you want to request.
		  DEBUG: If set to True, will print debug messages to the console. Defaults to False

		Returns:
		  Nothing is being returned.
		"""
		self.logger = Logger("APIKeyRegister",DEBUG=DEBUG)
		if apiKeys is None:
			self.requestedKeys = []
		if apiKeys:
			self.requestedKeys = apiKeys
			self.keysFile = "./config.toml"
			self.loadConfig()
		else:
			self.logger.debugMsg("Called without keys being requested")
			return None

	def loadConfig(self):
		"""
		It loads the api keys configured in config.toml
		"""
		with open(self.keysFile,"r"):
			self.keys = toml.load(self.keysFile,)["API"]
			print(self.keys)

	def getKeys(self, _returnDict={}) -> dict:
		"""
		> This function returns a dictionary of api names and their keys

		Args:
		  _returnDict: This is the dictionary that will be returned.

		Returns:
		  A dictionary with the requested keys.
		"""
		# sourcery skip: default-mutable-arg
		for keyname in self.requestedKeys:
			try:
				_returnDict[str(keyname)] = self.keys[keyname.lower()]
			except (KeyError):
				_returnDict[str(keyname)] = None
		self.logger.debugMsg(f"Found Keys:{[key for key in list(_returnDict.keys()) if key is None]} Missing Keys:{[key for key in list(_returnDict.keys()) if key is not None]}")
		return _returnDict