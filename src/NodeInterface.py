class NodeInterface():
	def __init__(self,nodeEditor,debug=False) -> None:
		self.NE = nodeEditor
		pass

	def visualize(self,root):
		layers = self.splitIntoLayers(root)
		print(layers)

	def splitIntoLayers(self,root):
		layers = {0:[root]}
		layers[1] = root._children
		return self.IterateTree(layers)

	def IterateTree(self,layers,layerIndex = 1):
		layerList = []
		for node in layers[layerIndex]:
			if len(node._children) >= 1:
				layerList.extend(node._children)
		if layerList:
			layers[layerIndex + 1] = layerList
			return self.IterateTree(layers,layerIndex=layerIndex + 1)
		else:
			return layers

if __name__ == "__main__":
	class Node():
		def __init__(self,title,color=None,debug=False) -> None:
			# self.logger = Logger(f"Node({title})",debug=debug)
			self.data = {
				"title":title,
				"data":[],
				"image":None,
			}
			self._children = []

		def addDataField(self,datatype,data):
			self.data["data"].append({datatype:data})

		def removeDataField(self,datatype,data):
			self.data["data"].remove({datatype:data})

		def addImage(self,imagetype,imageUrl):
			self.data["image"] = {imagetype:imageUrl}

	test = Node("root")
	child1 = Node("c1") #layer0
	child1_1 = Node("c1_1") #layer1
	child1_1_1 = Node("c1_1_1") #layer2
	child1_1._children.append(child1_1_1)
	child1_2 = Node("c1_2") #layer1
	child1._children.extend([child1_1,child1_2])
	child2 = Node("c2") #layer0
	child2_1 = Node("c2_1") #layer1
	child2_2 = Node("c2_2") #layer1
	child2._children.extend([child2_1,child2_2])
	test._children.extend([child1,child2])

	node = NodeInterface("none")
	node.visualize(test)