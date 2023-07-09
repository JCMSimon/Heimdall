import dearpygui.dearpygui as dpg
from os import walk
from src.Logger import Logger
from screeninfo import get_monitors

class GUI():
	def __init__(self,debug=False) -> None:
		self.logger = Logger("GUI",DEBUG=debug)
		dpg.create_context()
		dpg.create_viewport(title="Heimdall", min_width=1100, min_height=700, width=1100, height=700)
		dpg.setup_dearpygui()
		self.initStyles()
		self.loadTextures()
		self.mainWindow = dpg.add_window(label="Heimdall",on_close=self.closeGUI,horizontal_scrollbar=False,no_title_bar=True,no_scrollbar=True,no_collapse=True,no_close=False,no_resize=True,menubar=False,no_move=True,height=dpg.get_viewport_height(),width=dpg.get_viewport_width())
		dpg.set_primary_window(self.mainWindow,True)
		dpg.set_frame_callback(1,callback=lambda: self.switchState("MAIN"))
		self.centerViewport()
		dpg.show_viewport()
		dpg.start_dearpygui()

	def initStyles(self):
		with dpg.theme() as global_theme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (13, 17, 23), category=dpg.mvThemeCat_Core)
			with dpg.theme_component(dpg.mvImageButton):
				dpg.add_theme_color(dpg.mvThemeCol_Button, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0,0,0,0), category=dpg.mvThemeCat_Core)
		dpg.bind_theme(global_theme)

	def loadTextures(self):
		for (_, _, filenames) in walk("./src/gui/assets/main"):
			assets = [filename for filename in filenames if filename.endswith(".png")]
			break
		self.textures = {}
		with dpg.texture_registry():
			for asset in assets:
				width, height, _, data = dpg.load_image(f"./src/gui/assets/main/{asset}")
				self.textures[asset.replace(".png","")] = dpg.add_dynamic_texture(width, height, data)

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
				# Structure
				dpg.add_image(texture_tag=self.textures["title"],parent=self.mainWindow,pos=[251,198])
				newButton = dpg.add_image_button(label="button-new",texture_tag=self.textures["button-new"],parent=self.mainWindow,pos=[255,342],callback=lambda: self.switchState("SEARCH"))
				loadBUtton = dpg.add_image_button(label="button-load",texture_tag=self.textures["button-load"],parent=self.mainWindow,pos=[510,342],callback=lambda: self.switchState("LOAD"))
				settingsButton = dpg.add_image_button(label="button-settings",texture_tag=self.textures["button-settings"],parent=self.mainWindow,pos=[765,342],callback=lambda: self.switchState("SETTINGS"))
				# Event
				with dpg.item_handler_registry() as buttonHandler:
					dpg.add_item_hover_handler(callback=self.buttonHoverCallback)
				dpg.bind_item_handler_registry(newButton,buttonHandler)
				dpg.bind_item_handler_registry(loadBUtton,buttonHandler)
				dpg.bind_item_handler_registry(settingsButton,buttonHandler)
			case "SEARCH":
				dpg.add_button(label="search ui",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))
			case "LOADING":
				dpg.add_button(label="loading while searching",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))
			case "VIEW":
				dpg.add_button(label="view results",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))
			case "LOAD":
				dpg.add_button(label="load a saved file",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))
			case "SETTINGS":
				dpg.add_button(label="adjust settings",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))
			case _:
				dpg.add_button(label="wtf",parent=self.mainWindow,callback=lambda: self.switchState("MAIN"))

	def buttonHoverCallback(self, _, app_data):
		pass
		# while dpg.is_item_hovered(app_data):
			# print("wait")
		# print("bye")


	def resetToDefault(self):
		for item in dpg.get_item_children(self.mainWindow)[children_index := 1]:
			dpg.delete_item(item)

	def closeGUI(self):
		dpg.destroy_context()
