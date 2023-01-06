from src.Logger import Logger
import dearpygui.dearpygui as dpg
class NodeInterface():
	def __init__(self,nodeEditor,debug=False) -> None:
		self.logger = Logger("NodeInterface",debug=debug)
		self.NE = nodeEditor
		self.initTheme()

	def initTheme(self):
		with dpg.theme() as self.nodeTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvNodeStyleVar_NodeCornerRounding,0)

	def convert(self,root):
		nonDPGLayers = self.splitIntoLayers(root)
		self.layerDPGNodes = self.convertLayersToDPG(nonDPGLayers)
		dpg.set_frame_callback(dpg.get_frame_count() + 1,self.visualize)

	def visualize(self):
		layerHeights = {}
		for layerIndex in self.layerDPGNodes:
			heights = set()
			for node in self.layerDPGNodes[layerIndex]:
				heights.add(dpg.get_item_rect_max(node)[1])
			layerHeights[layerIndex] = max(heights)
		print(layerHeights)

	def convertLayersToDPG(self,layers):
		dpgLayers = {}
		for index in range(0,len(layers)):
			dpgLayers[index] = []
			for node in layers[index]:
				for field in node.data["data"]:
					for key,value in field.items():
						with dpg.node(parent=self.NE,label=f"{node.data['title']}") as node:
							with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
								dpg.add_text(value)
						dpgLayers[index].append(node)
		return dpgLayers


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