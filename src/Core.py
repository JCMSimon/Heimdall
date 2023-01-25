import string
from time import strftime
from src.NodeInterface import NodeInterface
from src.Logger import Logger
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node
import pickle
import os
from dearpygui.dearpygui import get_item_children,delete_item,split_frame

class Core():
	def __init__(self,pluginRegister,nodeEditor,debug=False) -> None:
		self.debug = debug
		self.logger = Logger("Core",debug=self.debug)
		self.pluginRegister = pluginRegister
		self.nodeInterFace = NodeInterface(nodeEditor,debug=debug)

	def search(self,datatype,keyword):
		#TODO later on it should already ask for all plugins to be ran that accept the type that is input
		#TODO have plugins define a default input type
		self.logger.debugMsg(f"Searching '{keyword}' as '{datatype}'")
		# Create root node
		self.root = Node("ROOT", debug=self.debug)
		self.root.addDataField(dp._internal.is_root_node,True)
		# First Search
		initialResults = self.pluginRegister.runPlugin(datatype,keyword)
		self.root._children.extend(initialResults)
		self.todo = initialResults
		# Recursive search
		while self.todo:
			for node in self.todo:
				for dataField in node.data["data"]: # this might be wrong syntax. it should loop through data fields
					for datatype,data in dataField.items():
						plugins = self.pluginRegister.getPluginNamesByType(datatype)
						results = []
						for plugin in plugins:
							try:
								results.extend(self.pluginRegister.runPlugin(plugin,data))
							except (TypeError,IndexError):
								self.logger.infoMsg(f"{plugin} returned no results")
				node._children.extend(results)
				self.todo.extend(results)
				self.todo.remove(node)
		# Visualize whole Tree
		self.nodeInterFace.visualize(self.root)

	def reloadPlugins(self):
		self.pluginRegister.reload()

	def save(self,filename):
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

	def load(self,filename):
		path = f"./saves/{filename}.pickle"
		self.logger.debugMsg(f"Loading from {path}")
		self.root = None
		with open(path,"rb") as picklefile:
			try:
				self.root = pickle.load(picklefile)
			except EOFError:
				self.logger.errorMsg("Cant load empty File")

		for node in get_item_children(self.nodeInterFace.NE)[1]:
			delete_item(node)
		if self.root:
			self.nodeInterFace.visualize(self.root)

	def deleteSave(self,filename):
		path = f".\saves\{filename}.pickle"
		if os.path.exists(path):
			os.system(f"del {path}")
			return True
		else:
			self.logger.errorMsg(f"There is no Save at {path}")
			return False

# Thanks to https://gist.github.com/seanh/93666 !
def format_filename(s):
	"""Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
	valid_chars = f"-_ {string.ascii_letters}{string.digits}"
	filename = ''.join(c for c in s if c in valid_chars)
	return filename.replace(' ','_')