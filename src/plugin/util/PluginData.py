import hashlib
import pickle
from typing import Any

from src.Logger import Logger


class PluginData:
	"""Utility for plugins to save and load arbitrary data"""
	def __init__(self, key, debug=True) -> None:
		"""
		The function takes a key, and then creates a new key by appending the hash of the key to the key.

		The function then loads the file.

		Args:
		  key: The key to the data.
		  debug: If True, it will print out the data in the file. Defaults to True
		"""
		self.logger = Logger("PluginDatat")
		self.realKey = str(key) + self.hashKey(key)
		self.data = self.loadFile()

	def loadFile(self) -> dict:
		"""
		It loads a pickle file and returns the data in it

		Returns:
		  The data from the file or an empty dictionary if the file doesn't exist.
		"""
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

	def getKey(self,key) -> Any | None:
		"""
		> If the key exists in the dictionary, return the value, otherwise dont return

		Args:
		  key: The key to get the value for

		Returns:
		  The value of the key if available.
		"""
		try:
			return self.data[key]
		except KeyError:
			self.logger.infoMsg(f"No Value found for key:{key}")

	def setKey(self,key,value) -> None:
		"""
		It takes a key and a value, and then it sets the key to the value in the data dictionary

		Args:
		  key: The key to store the data under.
		  value: The value you want to set the key to.
		"""
		path = f"./pluginData/{self.realKey}.pickle"
		self.data[key] = value
		with open(path,"wb") as picklefile:
			pickle.dump(self.data,picklefile)

	def hashKey(self,word) -> str:
		"""
		It takes a string, converts it to bytes, hashes it, and returns the first 8 characters of the hash

		Args:
		  word: The word to be hashed

		Returns:
		  The first 8 characters of the hash of the word.
		"""
		output = hashlib.sha256(word.encode()).hexdigest()
		return str(output[:8])