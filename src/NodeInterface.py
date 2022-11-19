class NodeInterface():
	def __init__(self,nodeEditor,debug=False) -> None:
		self.NE = nodeEditor
		pass

	def visualize(self,tree):
		print(tree._children)
		for child in tree._children:
			print("##" + str(child._children))