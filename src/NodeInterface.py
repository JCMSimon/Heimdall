from src.Logger import Logger
import dearpygui.dearpygui as dpg
import jsonpickle
class NodeInterface():
	def __init__(self,nodeEditor,XGap=10,YGap=10,debug=False) -> None:
		self.logger = Logger("NodeInterface",debug=debug)
		self.NE = nodeEditor
		self.XGap = XGap
		self.YGap = YGap

	def visualize(self,root):
		if not root:
			return
		layers = self.splitIntoLayers(root)
		self.assignDPGIds(layers)
		layerHeights,layerWidths = self.getLayerDimensions(layers)
		self.drawLayers(layers,layerHeights,layerWidths)

	def drawLayers(self,layers,layerHeights,layerWidths):
		editorMiddleX = dpg.get_item_rect_size(self.NE)[0] / 2
		for layerId in range(len(layers)):
			x = round(editorMiddleX - ((layerWidths[layerId]) / 2))
			y = sum(list(layerHeights.values())[:layerId]) + len(list(layerHeights.values())[:layerId]) + (self.YGap * layerId)
			for node in layers[layerId]:
				dpg.set_item_pos(node.data["DPGId"],[x,y])
				dpg.show_item(node.data["DPGId"])
				x += self.XGap + dpg.get_item_rect_size(node.data["DPGId"])[0]

	def getLayerDimensions(self,layers):
		layerHeights = {}
		layerWidths = {}
		for layerId in range(len(layers)):
			layerHeights[layerId] = max(dpg.get_item_rect_size(node.data["DPGId"])[1] for node in layers[layerId])
			layerWidths[layerId] = sum(dpg.get_item_rect_size(node.data["DPGId"])[0] for node in layers[layerId]) + ((len(layers[layerId]) - 1) * self.XGap)
			nodeIds = [node.data["DPGId"] for node in layers[layerId]]
			for nodeId in nodeIds:
				dpg.hide_item(nodeId)
		return layerHeights,layerWidths

	def assignDPGIds(self,layers):
		for layerID in range(len(layers)):
			for node in layers[layerID]:
				for field in node.data["data"]:
					for key,value in field.items():
						with dpg.node(
							parent=self.NE,
							label=f"{node.data['title']}") as nodeID:
							node.data["DPGId"] = nodeID
							if node.data['title'] != "ROOT":
								with dpg.node_attribute(
									attribute_type=dpg.mvNode_Attr_Static):
									dpg.add_text(value)
				dpg.split_frame()

	def splitIntoLayers(self,root):
		layers = {0: [root], 1: root._children}
		return self.IterateTree(layers)

	def IterateTree(self,layers,layerIndex = 0):
		layerList = []
		for node in layers[layerIndex]:
			if len(node._children) >= 1:
				layerList.extend(node._children)
				for childNode in node._children:
					childNode.data["parent"] = node
		if layerList:
			layers[layerIndex + 1] = layerList
			return self.IterateTree(layers,layerIndex=layerIndex + 1)
		else:
			return layers