import toml
from Logger import Logger

class KeyRegister:
	def __init__(self,apiKeys=[],debug=True) -> None:
		self.logger = Logger("KeyRegister",debug=debug)
		self.keysFile = "config.toml"
		self.loadConfig()

	def loadConfig(self):
		with open(self.keysFile,"r") as file:
			self.keys = toml.load(self.keysFile,)["API"]

	def returnKeys(self,apiKeys):
		returnDict = {}
		for keyname in apiKeys:
			try:
				returnDict[f"{keyname}"] = self.keys[keyname.lower()]
				self.logger.debugMsg(f"Found key for {keyname}")
			except KeyError:
				returnDict[f"{keyname}"] = None
				self.logger.debugMsg(f"No key for {keyname}")
		return returnDict