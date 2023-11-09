import os
import pathlib
import pickle
from string import ascii_letters,digits
from time import strftime
from typing import LiteralString

from src.PluginRegister import PluginRegister
from plugins._lib.Data import datapoints as dp
from plugins._lib.Node import Node
from src.Logger import Logger

class Core():
	def __init__(self,DEBUG=False) -> None:
		self._DEBUG = DEBUG
		self.logger = Logger("Core",DEBUG=self._DEBUG)
		self.pluginRegister = PluginRegister(DEBUG=self._DEBUG)
		if not os.path.exists("./saves"):
			os.system("mkdir saves")

	def search(self,datapoint,keyword,feedbackFunc=None) -> Node:
		self.ff = self.logger.infoMsg if feedbackFunc is None else feedbackFunc		
		self.rootNode = Node("ROOT", debug=self._DEBUG).addDataField(dp._internal.is_root_node,True)
		# Using a fake node as a starting point
		FakeNode = Node("F4K3")
		FakeNode.addDataField(datapoint,keyword)
		todo = [FakeNode]
		return self._recursiveSearch(todo)

	def _recursiveSearch(self,todo) -> Node:
		for node in todo:
			for datapoint in node.datapoints:
				for datatype,data in datapoint.items():
					plugins = self.pluginRegister.getPluginNamesByDatatype(datatype)
					results = []
					for plugin in plugins:
						self.ff(f"Running plugin: {plugin}")
						results.extend(self.pluginRegister.runPlugin(plugin,data))
			if node.title == "F4K3":
				self.rootNode._children.extend(results) 
			else:
				node._children.extend(results) 
			todo.extend(results) 
		return self.rootNode 

	def createSave(self,filename) -> str:
		formatted_filename = format_filename(filename)
		# If the File nam would be empty, replace it with a timestamp
		filename = strftime("%Y%m%d-%H%M%S") if filename.strip() == "" else formatted_filename
		path = f"./saves/{filename}.pickle"
		if self.rootNode is None:
			self.logger.infoMsg("No data to save")
		else:
			self.logger.infoMsg(f"Saving to {path}")
			with open(path,"wb") as picklefile:
				pickle.dump(self.rootNode,picklefile)
				return filename

	def loadSave(self,filename) -> None:
		"""
		It loads a save file and sets the Core root to the loaded object

		Args:
		  filename: The name of the file to load.
		"""
		path = f"./saves/{filename}.pickle"
		self.logger.debugMsg(f"Loading from {path}")
		self.rootNode = None
		try:
			with open(path,"rb") as picklefile:
				try:
					self.rootNode = pickle.load(picklefile)
					return self.rootNode
				except EOFError:
					self.logger.errorMsg("Cant load empty File")
		except FileNotFoundError:
				self.logger.errorMsg("File does not exist")

	def deleteSave(self,filename) -> bool:
		"""
		It deletes a save file

		Args:
		  filename: The name of the save file.

		Returns:
		  A boolean value. True if file was deleted successfuly. False if not.
		"""
		CurrentDir = pathlib.Path(__file__).parent.parent.absolute()
		path = f"{CurrentDir}\saves\{filename}.pickle"
		if os.path.exists(path):
			self.logger.debugMsg(f"Trying to delete '{CurrentDir}\saves\{filename}.pickle'")
			os.system(f'del "{path}"')
			return True
		else:
			self.logger.errorMsg(f"There is no save at {path}")
			return False

	def getAvailableDatapoints(self) -> set:
		"Simple passthrough method"
		return self.pluginRegister.getAvailableDatapoints()

# Thanks to https://gist.github.com/seanh/93666 !
def format_filename(filename) -> LiteralString:
	"""
	It takes a string and returns a string that is a valid filename

	Args:
	  name: The string to be formatted

	Returns:
	  A string that is a valid filename
	"""
	valid_chars = f"-_ {ascii_letters}{digits}"
	filename = ''.join(char for char in filename if char in valid_chars)
	return filename.replace(' ','_')