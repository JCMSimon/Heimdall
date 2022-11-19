import json

class NodeInterface():
	def __init__(self,nodeEditor,debug=False) -> None:
		self.NE = nodeEditor
		pass

	def visualize(self,tree):
		pass

	def dump(self,tree):
		with open("test.json","w") as file:
			json.dump(tree,file,default=str)