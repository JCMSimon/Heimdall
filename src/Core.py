import string
from time import strftime
from typing import LiteralString
from src.Logger import Logger
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node
import pickle
import os
from dearpygui.dearpygui import get_item_children,delete_item,split_frame

class Core():
	"""Heimdall's Core. responsible for the search process"""
	def __init__(self,pluginRegister,DEBUG=False) -> None:
		self._DEBUG = DEBUG
		self.logger = Logger("Core",DEBUG=self._DEBUG)
		self.pluginRegister = pluginRegister

	def search(self,pluginName,keyword) -> None:
		self.root = Node("ROOT", debug=self.debug).addDataField(dp._internal.is_root_node,True)
		datapoint = self.pluginRegister.getDefaultDatapointByName(pluginName)



		# self.root._children.extend(initialResults)
		# self.todo = initialResults
		# Recursive search
		# while self.todo:
		# 	for node in self.todo:
		# 		for dataField in node.data["data"]: # this might be wrong syntax. it should loop through data fields
		# 			for datatype,data in dataField.items():
		# 				plugins = self.pluginRegister.getPluginNamesByType(datatype)
		# 				results = []
		# 				for plugin in plugins:
		# 					try:
		# 						results.extend(self.pluginRegister.runPlugin(plugin,data))
		# 					except (TypeError,IndexError):
		# 						self.logger.infoMsg(f"{plugin} returned no results")
		# 		node._children.extend(results)
		# 		self.todo.extend(results)
		# 		self.todo.remove(node)


	def save(self,filename) -> None:
		"""
		It saves the current state of the program to a file

		Args:
		  filename: The name of the file to save to.
		"""
		try:
			filename = format_filename(filename)
			if filename == "":
				filename = strftime("%Y%m%d-%H%M%S")
			path = f"./saves/{filename}.pickle"
			self.logger.debugMsg(f"Saving to {path}")
			split_frame()
			with open(path,"wb") as picklefile:
				pickle.dump(self.root,picklefile)
		except AttributeError:
			self.logger.infoMsg("No data to save")

	def load(self,filename) -> None:
		"""
		It loads a pickle file and then deletes all the nodes in the treeview.

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
			else:
				for node in get_item_children(self.nodeInterFace.NE)[1]:
					delete_item(node)
		if self.root:
			self.nodeInterFace.visualize(self.root)

	def deleteSave(self,filename) -> bool:
		"""
		It deletes a file from the saves folder.

		Args:
		  filename: The name of the file you want to delete.

		Returns:
		  The return value is a boolean value.
		"""
		path = f".\saves\{filename}.pickle"
		if os.path.exists(path):
			os.system(f"del {path}")
			return True
		else:
			self.logger.errorMsg(f"There is no Save at {path}")
			return False

# Thanks to https://gist.github.com/seanh/93666 !
def format_filename(s) -> LiteralString:
	"""
	It takes a string and returns a valid filename, replacing spaces with underscores

	Args:
	  s: the string to be formatted

	Returns:
	  the filename with the spaces replaced with underscores.
	"""
	valid_chars = f"-_ {string.ascii_letters}{string.digits}"
	filename = ''.join(c for c in s if c in valid_chars)
	return filename.replace(' ','_')