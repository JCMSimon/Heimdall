import os
import pickle
import string
from time import strftime
from typing import LiteralString

from tqdm import tqdm

from src.PluginRegister import PluginRegister
from plugins._lib.Data import datapoints as dp
from plugins._lib.Node import Node
from src.Logger import Logger


class Core():
	"""Heimdall's Core. responsible for the search process"""
	def __init__(self,DEBUG=False) -> None:
		"""
		This function initializes the Core class

		Args:
		  pluginRegister: This is the plugin register that the core will use to execute plugins.
		  DEBUG: If set to True, the logger will print out debug messages. Defaults to False
		"""
		self._DEBUG = DEBUG
		self.logger = Logger("Core",DEBUG=self._DEBUG)
		self.pluginRegister = PluginRegister(DEBUG=self._DEBUG)

	def search(self,datapoint,keyword) -> Node:
		"""
		> The function takes a plugin name and a keyword, and returns a list of nodes that are the result of
		the search

		Args:
		  datapoint: a defined data point.
		  keyword: The keyword to search for

		Returns:
		  A list of nodes.
		"""
		self.root = Node("ROOT", debug=self._DEBUG).addDataField(dp._internal.is_root_node,True)
		todo = [Node("F4K3").addDataField(datapoint,keyword)]
		return self._recursiveSearch(todo)

	def _recursiveSearch(self,todo) -> Node:
		"""
		It takes a list of nodes, and for each node, it runs all plugins that are registered for the
		datatype of the node's data, and then adds the results of those plugins to the node's children

		Args:
		  todo: A list of nodes to process
		  pbar: The progress bar object

		Returns:
		  A Tree of nodes
		"""
		# pbar = getPbar(todo,"Processing Nodes","Nodes")
		for node in todo:
			for dataField in node.data["data"]:
				for datatype,data in dataField.items():
					plugins = self.pluginRegister.getPluginNamesByDatapoint(datatype)
					results = []
					for plugin in plugins:
						results.extend(self.pluginRegister.runPlugin(plugin,data))
			if node.data["title"] == "F4K3":
				self.root._children.extend(results) # type: ignore
			else:
				node._children.extend(results) # type: ignore
			# pbar.update(1)
			# todo.extend(results) # type: ignore
			# pbar.total += len(results)
		# pbar.close()
		return self.root # type: ignore

	def createSave(self,filename) -> None:
		"""
		It saves the Core root to a file

		Args:
		  filename: The name of the file to save to.
		"""
		filename = format_filename(filename)
		# If the File nam would be empty, replace it with a timestamp
		if filename == "":
			filename = strftime("%Y%m%d-%H%M%S")
		path = f"./saves/{filename}.pickle"
		self.logger.debugMsg(f"Saving to {path}")
		if self.root is None:
			self.logger.infoMsg("No data to save")
		else:
			with open(path,"wb") as picklefile:
				pickle.dump(self.root,picklefile)

	def loadSave(self,filename) -> None:
		"""
		It loads a save file and sets the Core root to the loaded object

		Args:
		  filename: The name of the file to load.
		"""
		path = f"./saves/{filename}.pickle"
		self.logger.debugMsg(f"Loading from {path}")
		self.root = None
		with open(path,"rb") as picklefile:
			try:
				self.root = pickle.load(picklefile)
				return self.root
			except EOFError:
				self.logger.errorMsg("Cant load empty File")

	def deleteSave(self,filename) -> bool:
		"""
		It deletes a save file

		Args:
		  filename: The name of the save file.

		Returns:
		  A boolean value. True if file was deleted successfuly. False if not.
		"""
		path = f"./saves/{filename}.pickle" #TODO This might not work. gonna see in future
		if os.path.exists(path):
			os.system(f"del {path}")
			return True
		else:
			self.logger.errorMsg(f"There is no save at {path}")
			return False

	def getAvailableDatapoints(self) -> set:
		return self.pluginRegister.getAvailableDatapoints()

# Thanks to https://gist.github.com/seanh/93666 !
def format_filename(name) -> LiteralString:
	"""
	It takes a string and returns a string that is a valid filename

	Args:
	  name: The string to be formatted

	Returns:
	  A string with the characters in the string s that are in the string valid_chars.
	"""
	valid_chars = f"-_ {string.ascii_letters}{string.digits}"
	filename = ''.join(c for c in name if c in valid_chars)
	return filename.replace(' ','_')

def getPbar(iterable,desc,unit,color="#7800C8") -> tqdm:
	"""
	`getPbar` is a function that returns a progress bar object from the `tqdm` library

	Args:
	  iterable: the iterable object you want to present
	  desc: The description of the progress bar
	  unit: The unit of the progress bar.
	  color: The color of the progress bar. Defaults to #7800C8

	Returns:
	  A progress bar object.
	"""
	return tqdm(total=len(iterable),ascii=True,desc=desc,leave=False,unit=unit,colour=color)