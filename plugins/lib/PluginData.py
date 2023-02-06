import hashlib
import pickle
from src.Logger import Logger

class PluginData:
	def __init__(self, key, debug=True) -> None:
		self.logger = Logger("PluginDatat")
		self.realKey = str(key) + self.hashKey(key)
		self.data = self.loadFile()

	def loadFile(self):
		path = f"./pluginData/{self.realKey}.pickle"
		try:
			with open(path,"rb") as picklefile:
				data = pickle.load(picklefile)
			return data or {}
		except FileNotFoundError:
			return {}
		except EOFError:
			self.logger.errorMsg("Plugin Data File Corrupted. Resetting")
			return {}

	def get(self,key):
		try:
			return self.data[key]
		except KeyError:
			self.logger.infoMsg(f"No Value found for key:{key}")

	def save(self,key,value):
		path = f"./pluginData/{self.realKey}.pickle"
		self.data[key] = value
		with open(path,"wb") as picklefile:
			pickle.dump(self.data,picklefile)

	def hashKey(self,word):
		output = hashlib.sha256(word.encode()).hexdigest()
		return str(output[:8])