from src.NodeInterface import NodeInterface
from src.Logger import Logger
from plugins.lib.Data import datapoints as dp
from plugins.lib.Node import Node

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
		self.root = Node(f"Searching '{keyword}' as '{datatype}'",debug=self.debug)
		self.root.addDataField(dp._internal.is_root_node,True)
		self.logger.debugMsg("First search iteration")
		initialResults = self.pluginRegister.runPlugin(datatype,keyword)
		self.logger.debugMsg(f"Results: {initialResults}")
		self.logger.debugMsg(f"Adding results to root node")
		self.root._children.extend(initialResults)
		self.todo = initialResults
		for node in self.todo:
			for dataField in node.data["data"]: # this might be wrong syntax. it should loop through data fields
				for datatype,data in dataField:
					plugins = self.pluginRegister.getPluginNamesByType(datatype)
					results = []
					for plugin in plugins:
						data = self.pluginRegister.runPlugin(plugin,keyword)
					results.append(data)
			node._children.extend(results)
			self.todo.extend(results)
	#TODO smth smth vosualise every now and then