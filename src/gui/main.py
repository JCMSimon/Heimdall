import dearpygui.dearpygui as dpg
from os import walk
from src.Logger import Logger
from screeninfo import get_monitors
from src.gui.lib.RelationalUI import RelationalNodeUI as RNUI
from src.Core import Core

class GUI():
	def __init__(self,DEBUG=False) -> None:
		self.logger = Logger("GUI",DEBUG=DEBUG)
		self.core = Core(DEBUG=DEBUG)
		dpg.create_context()
		dpg.create_viewport(title="Heimdall", min_width=1100, min_height=700, width=1100, height=700, decorated=False)
		dpg.setup_dearpygui()
		self.initStyles()
		self.loadTextures()
		self.mainWindow = dpg.add_window(label="Heimdall",on_close=self.closeGUI,horizontal_scrollbar=False,no_title_bar=True,no_scrollbar=True,no_collapse=True,no_close=False,no_resize=True,menubar=False,no_move=True,height=dpg.get_viewport_height(),width=dpg.get_viewport_width())
		dpg.set_primary_window(self.mainWindow,True)
		dpg.set_frame_callback(1,callback=lambda: self.switchState("SEARCH"))
		self.centerViewport()
		dpg.show_viewport()
		dpg.start_dearpygui()

	def initStyles(self):  # sourcery skip: extract-duplicate-method
		with dpg.theme() as global_theme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (13, 17, 23), category=dpg.mvThemeCat_Core)
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
			with dpg.theme_component(dpg.mvImageButton):
				dpg.add_theme_color(dpg.mvThemeCol_Button, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (13,17,23,75), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0,0,0,0), category=dpg.mvThemeCat_Core)
		with dpg.theme() as self.exit_button_theme:
			with dpg.theme_component(dpg.mvImageButton):
				dpg.add_theme_color(dpg.mvThemeCol_Button, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0,0,0,0), category=dpg.mvThemeCat_Core)
		with dpg.theme() as self.search_ui_theme:
			with dpg.font_registry():
				self.input_font = dpg.add_font(file="./src/gui/assets/fonts/Roboto-Regular.ttf",size=55)
			with dpg.theme_component(dpg.mvInputText):
				dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_Text, (73,50,154,255), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (73,50,154,100), category=dpg.mvThemeCat_Core)
			with dpg.theme_component(dpg.mvCombo):
				dpg.add_theme_color(dpg.mvThemeCol_Text, (73,50,154,255), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (255,255,255,10), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (13,17,23,255), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, (73,50,154,100), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, (73,50,154,200), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_Header, (255,255,255,127), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (73,50,154,100), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (73,50,154,255), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (73,50,154,200), category=dpg.mvThemeCat_Core)
				dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 15)
				dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 15)
				dpg.add_theme_style(dpg.mvStyleVar_PopupBorderSize, 0)
			with dpg.theme_component(dpg.mvImageButton):
				dpg.add_theme_color(dpg.mvThemeCol_Button, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0,0,0,0), category=dpg.mvThemeCat_Core)
		dpg.bind_theme(global_theme)

	def loadTextures(self):
		for (_, _, filenames) in walk("./src/gui/assets/main"):
			assets = [filename for filename in filenames if filename.endswith(".png")]
			break
		self.images = {}
		self.textures = {}
		for asset in assets:
			width, height, _, data = dpg.load_image(f"./src/gui/assets/main/{asset}")
			with dpg.texture_registry():
				self.textures[asset.replace(".png","")] = dpg.add_dynamic_texture(width,height,data)
				self.images[asset.replace(".png","")] = [width, height, data]

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
				dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["main-background"],parent=self.mainWindow,pos=[0,-100])
				dpg.add_image(texture_tag=self.textures["title"],parent=self.mainWindow,pos=[251,198])
				dpg.add_image_button(label="button-new",texture_tag=self.textures["button-new"],parent=self.mainWindow,pos=[255,342],callback=lambda: self.switchState("SEARCH"))
				dpg.add_image_button(label="button-load",texture_tag=self.textures["button-load"],parent=self.mainWindow,pos=[510,342]) #,callback=lambda: self.switchState("LOAD")
				dpg.add_image_button(label="button-settings",texture_tag=self.textures["button-settings"],parent=self.mainWindow,pos=[765,342]) #,callback=lambda: self.switchState("SETTINGS")
				# Style
				dpg.bind_item_theme(exit_button,self.exit_button_theme)
				# Function
				# TODO | Add a drag handler to the "bar" image to drag the window
			case "SEARCH":
				# Definition
				def searchCallback():
					# TODO | Put searching into a seperate thread and load "LOADING" state while thats going
					if results := self.core.search(dpg.get_value(data_type_selector),dpg.get_value(search_input)):
						self.results = results
						self.switchState("VIEW")
				# Structure
				dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["small-title"],parent=self.mainWindow,pos=[468,4])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["search-background"],parent=self.mainWindow,pos=[0,0])
				data_values = list(self.core.getAvailableDatapoints())
				data_values.sort()
				data_type_selector = dpg.add_combo(parent=self.mainWindow,items=data_values,pos=[95,320],width=245,default_value=data_values[0],no_arrow_button=True,popup_align_left=True,height_mode=dpg.mvComboHeight_Small,)
				search_input = dpg.add_input_text(parent=self.mainWindow,pos=[346,320],width=665,multiline=False,hint="Search",callback=searchCallback,on_enter=True)
				back_button = dpg.add_image_button(label="button-back",texture_tag=self.textures["button-back"],parent=self.mainWindow,pos=[489,396],callback=lambda: self.switchState("MAIN"))
				# Style
				dpg.bind_item_font(data_type_selector,self.input_font)
				dpg.bind_item_font(search_input,self.input_font)
				dpg.bind_item_theme(data_type_selector,self.search_ui_theme)
				dpg.bind_item_theme(search_input,self.search_ui_theme)
				dpg.bind_item_theme(back_button,self.search_ui_theme)
				# Function
			case "LOADING":
				# TODO | needs more work with an actual loader or whatever. maybe a debug console idfk
				dpg.add_image(texture_tag=self.textures["main-background"],parent=self.mainWindow,pos=[0,-100])
			case "VIEW":
				dpg.add_text(f"{self.results._children[0].data}",parent=self.mainWindow)
			case "LOAD":
				pass
			case "SETTINGS":
				pass
			case _:
				print("OHNO")

	def resetToDefault(self):
		for item in dpg.get_item_children(self.mainWindow)[children_index := 1]:
			dpg.delete_item(item)

	def closeGUI(self):
		dpg.destroy_context()

				# hovered
				# dpg.set_value(item=self.textures[dpg.get_item_label(item)],value=self.images[f"hovered-{dpg.get_item_label(item)}"][image_index := 2])
				# normal
				# dpg.set_value(item=self.textures[dpg.get_item_label(item)],value=self.images[dpg.get_item_label(item)][image_index := 2])
