from src.Logger import Logger
import dearpygui.dearpygui as dpg
class NodeInterface():
	def __init__(self,nodeEditor,debug=False) -> None:
		self.logger = Logger("NodeInterface",debug=debug)
		self.NE = nodeEditor

	def visualize(self,root):
		layers = self.splitIntoLayers(root)
		self.assignDPGIds(layers)
		

	def assignDPGIds(self,layers):
		for layerID in range(len(layers)):
			for node in layers[layerID]:
				for field in node.data["data"]:
					for key,value in field.items():
						with dpg.node(
							pos=[-9999,-9999],
							parent=self.NE,
							label=f"{node.data['title']}") as nodeID:
							node.data["DPGId"] = nodeID
							if node.data['title'] != "ROOT":
								with dpg.node_attribute(
									attribute_type=dpg.mvNode_Attr_Static):
									dpg.add_text(value)
				dpg.split_frame()
				dpg.hide_item(nodeID)
				print(dpg.get_item_rect_size(nodeID))


	def splitIntoLayers(self,root):
		layers = {0: [root], 1: root._children}
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