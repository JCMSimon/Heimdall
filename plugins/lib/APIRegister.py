import toml

from src.Logger import Logger


class APIRegister:
	def __init__(self, apiKeys=None, DEBUG=True) -> None:
		# self.logger = Logger("APIKeyRegister",DEBUG=DEBUG)
		if apiKeys is None:
			self.requestedKeys = []
		if apiKeys:
			self.requestedKeys = apiKeys
			self.keysFile = "config.toml"
			self.loadConfig()
		else:
			self.logger.infoMsg("Called without keys being requested")
			return None

	def loadConfig(self):
		with open(self.keysFile,"r"):
			self.keys = toml.load(self.keysFile,)["API"]
			print(self.keys)

	def getKeys(self, _returnDict={}) -> dict:
		# sourcery skip: default-mutable-arg
		for keyname in self.requestedKeys:
			try:
				_returnDict[str(keyname)] = self.keys[keyname.lower()]
			except (KeyError):
				_returnDict[str(keyname)] = None
		# self.logger.debugMsg(f"Found Keys:{[key for key in list(returnDict.keys()) if key is None]} Missing Keys:{[key for key in list(returnDict.keys()) if key is not None]}")
		print(f"Found Keys:{[key for key in list(_returnDict.keys()) if _returnDict[key] is not None]}")
		return _returnDict