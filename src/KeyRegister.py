import toml

class KeyRegister:
	def __init__(self,apiKeys) -> None:
		self.keysFile = "keys.toml"
		self.loadConfig()
		self.returnKeys(apiKeys)

	def loadConfig(self):
		with open(self.keysFile,"r") as file:
			self.keys = toml.load(self.keysFile,)

	def returnKeys(self,apiKeys):
		returnDict = {}
		for keyname in apiKeys:
			try:
				returnDict[f"{keyname}"] = self.keys[keyname.lower()]
			except KeyError:
				returnDict[f"{keyname}"] = None
		print(returnDict)


if __name__ == "__main__":
	test = KeyRegister(["SkidSearch","Dehashed","Testing"])