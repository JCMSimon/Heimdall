from src.NodeInterface import NodeInterface
from plugins.lib.Node import Node

class Core():
	def __init__(self,pluginRegister,nodeEditor,debug=False) -> None:
		self.pluginRegister = pluginRegister
		self.nodeInterFace = NodeInterface(nodeEditor,debug=debug)

	def search(self,datatype,keyword):
		# create parent node with search as text
		parent = Node("Search here")
		results = self.pluginRegister.runPlugin(datatype,keyword)
		#TODO later on it should already ask for all plugins to be ran that accept the type that is input
		#TODO have plugins define a default input type
		# add all plugin results as children to parent node
		parent._children.extend(results)
		# create todo list
		todo = []
		# for child in children:
		for child in parent._children:
		#	for data element in child
			for pair in child.data["data"]:
				for datatype,data in pair:
		#		run plugin and add result to result list
					children = self.pluginRegister.runPlugin("doesent","matter")
		#	add results as children to ""child""
			child._children.extend(children)
		#	save children to TODO list
			todo.extend(children)
		# for child in TODO list:
		for node in todo:
		#	for data element in child
			for pair in child.data["data"]:
				for datatype,data in pair:
		#		run plugin and add result to result list
					children = self.pluginRegister.runPlugin("doesent","matter")
		#	add results as children
			node._children.extend(children)
		#	save children to TODO list at the back
			todo.extend(children)
		pass