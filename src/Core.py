import os
import pickle
import string
from time import strftime
from typing import LiteralString

from tqdm import tqdm

from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node
from src.Logger import Logger


class Core():
	"""Heimdall's Core. responsible for the search process"""
	def __init__(self,pluginRegister,DEBUG=False) -> None:
		"""
		This function initializes the Core class

		Args:
		  pluginRegister: This is the plugin register that the core will use to execute plugins.
		  DEBUG: If set to True, the logger will print out debug messages. Defaults to False
		"""
		self._DEBUG = DEBUG
		self.logger = Logger("Core",DEBUG=self._DEBUG)
		self.pluginRegister = pluginRegister

	def search(self,pluginName,keyword) -> Node:
		"""
		> The function takes a plugin name and a keyword, and returns a list of nodes that are the result of
		the search

		Args:
		  pluginName: The name of the plugin to run.
		  keyword: The keyword to search for

		Returns:
		  A list of nodes.
		"""
		self.root = Node("ROOT", debug=self._DEBUG).addDataField(dp._internal.is_root_node,True)
		todo = []
		if datapoint := self.pluginRegister.getDefaultDatapointByName(pluginName) is None:
			todo.extend(self.pluginRegister.run(pluginName,keyword))
		else:
			todo.extend(Node("F4K3").addDataField(datapoint,keyword))
		return self.recursiveSearch(todo)

	def recursiveSearch(self,todo,pbar) -> Node:
		"""
		It takes a list of nodes, and for each node, it runs all plugins that are registered for the
		datatype of the node's data, and then adds the results of those plugins to the node's children

		Args:
		  todo: A list of nodes to process
		  pbar: The progress bar object

		Returns:
		  A Tree of nodes
		"""
		pbar = getPbar(todo,"Processing Nodes","Nodes")
		for node in todo:
			for dataField in node.data["data"]:
				for datatype,data in dataField.items():
					plugins = self.pluginRegister.getPluginNamesByDatapoint(datatype)
					results = []
					for plugin in plugins:
						results.extend(self.pluginRegister.runPlugin(plugin,data))
			if node.data["title"] == "F4K3":
				self.root._children.extend(results)
			else:
				node._children.extend(results)
			pbar.update(1)
			todo.extend(results)
			# pbar.total += len(results)
		pbar.close()
		return self.root

	def save(self,filename) -> None:
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

	def load(self,filename) -> None:
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
		path = f".\saves\{filename}.pickle"
		if os.path.exists(path):
			os.system(f"del {path}")
			return True
		else:
			self.logger.errorMsg(f"There is no save at {path}")
			return False

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