import dearpygui.dearpygui as dpg
from src.Logger import Logger
from screeninfo import get_monitors

class GUI():
	def __init__(self,debug=False) -> None:
		self.logger = Logger("GUI",DEBUG=debug)
		dpg.create_context()
		dpg.create_viewport(title="Heimdall", min_width=1100, min_height=700, width=1100, height=700)
		dpg.setup_dearpygui()
		self.initDPGThemes()
		self.mainWindow = dpg.add_window(label="Heimdall",on_close=self.closeGUI,horizontal_scrollbar=False,no_title_bar=True,no_scrollbar=True,no_collapse=True,no_close=False,no_resize=True,menubar=False,no_move=True,height=dpg.get_viewport_height(),width=dpg.get_viewport_width(),)
		dpg.set_primary_window(self.mainWindow,True)
		dpg.set_frame_callback(1,callback=lambda: self.switchState("MAIN"))
		dpg.show_viewport()
		self.centerViewport()
		dpg.start_dearpygui()

	def initDPGThemes(self):
		with dpg.font_registry():
			self.titleFont = dpg.add_font("assets/fonts/Thor.ttf", 150)

	def centerViewport(self):
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos(pos=[(monitor_xd - dpg.get_viewport_width()) / 2,(monitor_yd - dpg.get_viewport_height()) / 2,])

	def switchState(self,GUIState):
		self.resetToDefault()
		match GUIState:
			case "MAIN":
				titleText = dpg.add_text(parent=self.mainWindow,color=(150,10,150),default_value="HEIMDALL")
				dpg.bind_item_font(item=titleText,font=self.titleFont)
				newButton = dpg.add_button(label="NEW",parent=self.mainWindow)
				loadButton = dpg.add_button(label="LOAD",parent=self.mainWindow)
				settingsButton = dpg.add_button(label="SETTINGS",parent=self.mainWindow)
				centerHorizontally(titleText,self.mainWindow,0)
				centerHorizontally(newButton,self.mainWindow,100)
				centerHorizontally(loadButton,self.mainWindow,120)
				centerHorizontally(settingsButton,self.mainWindow,140)
			case "SEARCH":
				dpg.add_button(label="search ui",parent=self.mainWindow)
			case "LOADING":
				dpg.add_button(label="loading while searching",parent=self.mainWindow)
			case "VIEW":
				dpg.add_button(label="view results",parent=self.mainWindow)
			case "LOAD":
				dpg.add_button(label="load a saved file",parent=self.mainWindow)
			case "SETTINGS":
				dpg.add_button(label="adjust settings",parent=self.mainWindow)
			case _:
				print("ohoh")

	def resetToDefault(self):
		for item in dpg.get_item_children(self.mainWindow)[children_index := 1]:
			dpg.delete_item(item)

	def closeGUI(self):
		dpg.destroy_context()

def centerHorizontally(item,container,y_pos):
	containerWidth = dpg.get_item_rect_size(container)[0]
	itemWidth = dpg.get_item_rect_size(item)[0]
	dpg.set_item_pos(item,[containerWidth / 2 - itemWidth / 2,y_pos])
