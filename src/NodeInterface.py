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

	def visualize(self,root):
		nonDPGLayers = self.splitIntoLayers(root)
		layerDPGNodes = self.convertLayersToDPG(nonDPGLayers)
		dpg.split_frame()
		layerHeights = self.getLayerHeights(layerDPGNodes)
		# offset = dpg.get_item_pos(layerDPGNodes[0][0])[0]
		offset = 0
		direction = 1
		for layer,_ in layerHeights.items():
			for node in layerDPGNodes[layer]:
				if layer == 0:
					test = dpg.get_item_rect_size(self.NE)
					dpg.set_item_pos(node,[test[0] / 2 - dpg.get_item_rect_size(node)[0] / 2,0])
				else:
					self.gap = 5
					#TODO HAVE GAP SETTING SOMEWHERE
					dpg.set_item_pos(
						node,
						[
						(dpg.get_item_pos(layerDPGNodes[0][0])[0]) + (dpg.get_item_rect_size(layerDPGNodes[0][0])[0] / 2) - (dpg.get_item_rect_size(node)[0] / 2) + (offset * direction),
						layerHeights[layer - 1] + self.gap
						]
					)
					try:
						offset = dpg.get_item_rect_size(prevnode)[0]
					except UnboundLocalError:
						offset = dpg.get_item_rect_size(node)[0]
					prevnode = node
					direction *= -1


	def getLayerHeights(self,layerDPGNodes):
		layerHeights = {}
		for layerIndex in layerDPGNodes:
			heights = set()
			for node in layerDPGNodes[layerIndex]:
				heights.add(dpg.get_item_rect_size(node)[1])
			layerHeights[layerIndex] = max(heights)
		return layerHeights

	def convertLayersToDPG(self,layers):
		dpgLayers = {}
		for index in range(0,len(layers)):
			dpgLayers[index] = []
			for node in layers[index]:
				for field in node.data["data"]:
					for key,value in field.items():
						with dpg.node(parent=self.NE,label=f"{node.data['title']}") as nodeID:
							if node.data['title'] != "ROOT":
								with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
									dpg.add_text(value)
						dpgLayers[index].append(nodeID)
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