import dearpygui.dearpygui as dpg
from os import walk
from src.Logger import Logger
from screeninfo import get_monitors
from src.gui.lib.RelationalUI import RelationalNodeUI
from src.Core import Core
import time
import threading

class GUI():
	def __init__(self,DEBUG=False) -> None:
		self.DEBUG = DEBUG
		self.logger = Logger("GUI",DEBUG=DEBUG)
		self.core = Core(DEBUG=DEBUG)
		dpg.create_context()
		dpg.create_viewport(title="Heimdall", min_width=1100, min_height=700, width=1100, height=700, decorated=False, vsync=True)
		dpg.setup_dearpygui()
		self.initStyles()
		self.loadTextures()
		self.mainWindow = dpg.add_window(label="Heimdall",on_close=self.closeGUI,horizontal_scrollbar=False,no_title_bar=True,no_scrollbar=True,no_collapse=True,no_close=False,no_resize=True,menubar=False,no_move=True)
		dpg.set_primary_window(self.mainWindow,True)
		dpg.set_frame_callback(1,callback=lambda: self.switchState("MAIN"))
		self.running = True
		self.is_menu_bar_clicked = True
		with dpg.handler_registry():
			dpg.add_mouse_drag_handler(button=0, threshold=0, callback=self.mouse_drag_callback)
			dpg.add_mouse_click_handler(button=0, callback=self.mouse_click_callback)
		self.centerViewport()
		dpg.show_viewport()
		dpg.start_dearpygui()

	def initStyles(self):  # sourcery skip: extract-duplicate-method
		with dpg.font_registry():
			self.input_font = dpg.add_font(file="./src/gui/assets/fonts/Roboto-Regular.ttf",size=55)
			self.file_name_font = dpg.add_font(file="./src/gui/assets/fonts/Roboto-Regular.ttf",size=30)
		with dpg.theme() as global_theme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (13, 17, 23), category=dpg.mvThemeCat_Core)
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 0, category=dpg.mvThemeCat_Core)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, category=dpg.mvThemeCat_Core)
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
		with dpg.theme() as self.view_ui_theme:
			with dpg.theme_component(dpg.mvInputText):
				dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (0,0,0,0), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_Text, (73,50,154,255), category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, (73,50,154,100), category=dpg.mvThemeCat_Core)
		with dpg.theme() as self.loading_theme:
			with dpg.theme_component(dpg.mvText):
				dpg.add_theme_style(dpg.mvStyleVar_SelectableTextAlign, 0.5, category=dpg.mvThemeCat_Core)
				dpg.add_theme_color(dpg.mvThemeCol_Text, (73,50,154,255), category=dpg.mvThemeCat_Core)
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
		self.logger.debugMsg(f"Loaded Assets:")
		self.logger.debugMsg(f"Textures: {len(self.textures)}")
		self.logger.debugMsg(f"Images: {len(self.images)}")

	def centerViewport(self):
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos(pos=[(monitor_xd - dpg.get_viewport_width()) / 2,(monitor_yd - dpg.get_viewport_height()) / 2,])

	def switchState(self,GUIState):
		self.resetToDefault()
		self.logger.debugMsg(f"Switching state to {GUIState}")
		self.GUIState = GUIState
		match GUIState:
			case "MAIN":
				# Structure
				self.mainbar = dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["main-background"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["title"],parent=self.mainWindow,pos=[251,198])
				dpg.add_image_button(label="button-new",texture_tag=self.textures["button-new"],parent=self.mainWindow,pos=[255,342],callback=lambda: self.switchState("SEARCH"))
				dpg.add_image_button(label="button-load",texture_tag=self.textures["button-load"],parent=self.mainWindow,pos=[510,342]) #,callback=lambda: self.switchState("LOAD")
				dpg.add_image_button(label="button-settings",texture_tag=self.textures["button-settings"],parent=self.mainWindow,pos=[765,342]) #,callback=lambda: self.switchState("SETTINGS")
				# Style
				dpg.bind_item_theme(exit_button,self.exit_button_theme)
			case "SEARCH":
				# Function
				def searchCallback():
					datapoint = dpg.get_value(data_type_selector)
					value = dpg.get_value(search_input)
					self.searchData = [datapoint,value]
					self.logger.debugMsg(f"Starting search with dp:{datapoint},value:{value}")
					if self.DEBUG:
						self.startedSerchTime = time.time()
					self.switchState("LOADING")
				# Structure
				self.mainbar = dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["small-title"],parent=self.mainWindow,pos=[468,4])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["search-background"],parent=self.mainWindow,pos=[0,0])
				data_values = list(self.core.getAvailableDatapoints())
				data_values.sort()
				self.logger.debugMsg("Gathered all available datapoints:")
				self.logger.debugMsg(data_values)
				data_type_selector = dpg.add_combo(parent=self.mainWindow,items=data_values,pos=[95,320],width=245,default_value=data_values[0],no_arrow_button=True,popup_align_left=True,height_mode=dpg.mvComboHeight_Small,)
				search_input = dpg.add_input_text(parent=self.mainWindow,pos=[346,320],width=665,multiline=False,hint="Search",callback=searchCallback,on_enter=True)
				back_button = dpg.add_image_button(label="button-back",texture_tag=self.textures["button-back"],parent=self.mainWindow,pos=[489,396],callback=lambda: self.switchState("MAIN"))
				# Style
				dpg.bind_item_font(data_type_selector,self.input_font)
				dpg.bind_item_font(search_input,self.input_font)
				dpg.bind_item_theme(data_type_selector,self.search_ui_theme)
				dpg.bind_item_theme(search_input,self.search_ui_theme)
				dpg.bind_item_theme(back_button,self.search_ui_theme)
			case "LOADING":
				def setLoadingText(text):
					dpg.set_value(self.loadingText,text)
					dpg.split_frame()
					dpg.set_item_pos(self.loadingText,[580 - dpg.get_item_rect_size(self.loadingText)[0] / 2,353])
				self.mainbar = dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["small-title"],parent=self.mainWindow,pos=[468,4])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["loading-background"],parent=self.mainWindow,pos=[0,0])
				self.loadingText = dpg.add_text(default_value="",pos=[580,353],parent=self.mainWindow)
				dpg.bind_item_theme(self.loadingText,self.loading_theme)
				dpg.bind_item_font(self.loadingText,self.input_font)
				if results := self.core.search(self.searchData[0],self.searchData[1],feedbackFunc=setLoadingText):
						self.result = results
						self.logger.debugMsg(f"Got search results: {self.result}")
						self.switchState("VIEW")
			case "VIEW":
				def backToSearch():
					self.RNUI.stopInteractionThreads()
					self.switchState("SEARCH")
				def saveCallback(_, app_data):
					dpg.split_frame()
					self.core.createSave(dpg.get_value(file_name_field))
				# Structure
				self.mainbar = dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["small-title"],parent=self.mainWindow,pos=[468,4])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["main-background"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["view-background"],parent=self.mainWindow,pos=[79,111])
				dpg.add_image(texture_tag=self.textures["view-filename-background"],parent=self.mainWindow,pos=[395,52])
				file_name_field = dpg.add_input_text(parent=self.mainWindow,pos=[410,58],width=260,multiline=False,hint="Unsaved File")
				save_button = dpg.add_image_button(label="button-save",texture_tag=self.textures["button-save"],parent=self.mainWindow,pos=[611,52],callback=saveCallback)
				self.RNUI = RelationalNodeUI(parent=self.mainWindow,width=942,height=512,x=111,y=79,DEBUG=self.DEBUG)
				back_button = dpg.add_image_button(label="button-back",texture_tag=self.textures["button-back"],parent=self.mainWindow,pos=[489,635],callback=backToSearch)
				self.RNUI.visualize(self.result)
				if self.DEBUG:
					self.logger.debugMsg(f"Search took {round(time.time() - self.startedSerchTime,2)}s")
				# Style
				dpg.bind_item_theme(back_button,self.search_ui_theme)
				dpg.bind_item_font(file_name_field,self.file_name_font)
				dpg.bind_item_theme(file_name_field,self.view_ui_theme)
			case "LOAD":
				pass
			case "SETTINGS":
				pass
			case _:
				self.mainbar = dpg.add_image(texture_tag=self.textures["bar"],parent=self.mainWindow,pos=[0,0])
				dpg.add_image(texture_tag=self.textures["small-title"],parent=self.mainWindow,pos=[468,4])
				exit_button = dpg.add_image_button(label="button-exit",texture_tag=self.textures["button-exit"],parent=self.mainWindow,pos=[1060,5],callback=self.closeGUI)
				dpg.add_image(texture_tag=self.textures["404-background"],parent=self.mainWindow,pos=[0,0])
				back_button = dpg.add_image_button(label="button-back",texture_tag=self.textures["button-back"],parent=self.mainWindow,pos=[330,517],callback=lambda: self.switchState("MAIN"))
				dpg.bind_item_theme(back_button,self.search_ui_theme)





	# # TODO | some werid offset, ask dpg dc
	# def dragWindow(self, isDragging = False):
	# 	bar_x_range = range(0,1076)
	# 	bar_y_range = range(-20,16)
	# 	while self.running:
	# 		time.sleep(1 / int(dpg.get_frame_rate()))
	# 		if dpg.is_mouse_button_dragging(button=dpg.mvMouseButton_Left,threshold=0.05) and not isDragging and not dpg.is_mouse_button_released(button=dpg.mvMouseButton_Left):
	# 			isDragging = True
	# 			# allow start dragging for 2 ms
	# 			drag_ts_timeout = time.time() + 0.02
	# 		elif isDragging and not dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left):
	# 			isDragging = False
	# 		if isDragging:
	# 			if dpg.get_mouse_pos(local=True)[0] in bar_x_range and dpg.get_mouse_pos(local=True)[1] in bar_y_range:
	# 				if time.time() < drag_ts_timeout:
	# 					old_vp_pos = dpg.get_viewport_pos()
	# 					while dpg.is_mouse_button_down(button=dpg.mvMouseButton_Left):
	# 						delta = dpg.get_mouse_drag_delta()
	# 						dpg.set_viewport_pos([old_vp_pos[0] + delta[0],old_vp_pos[1] + delta[1]])
	# 						time.sleep(1 / int(dpg.get_frame_rate()))

	def mouse_drag_callback(self, _, app_data):
		if self.is_menu_bar_clicked:
			_, drag_delta_x, drag_delta_y = app_data
			viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
			new_pos_x = viewport_pos_x + drag_delta_x
			new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
			dpg.set_viewport_pos([new_pos_x, new_pos_y])

	def mouse_click_callback(self):
		self.is_menu_bar_clicked = True if dpg.get_mouse_pos(local=True)[0] in range(0,1076) and dpg.get_mouse_pos(local=True)[1] in range(-20,16) else False

	def resetToDefault(self):
		for item in dpg.get_item_children(self.mainWindow)[children_index := 1]:
			dpg.delete_item(item)

	def closeGUI(self):
		if self.GUIState == "VIEW":
			self.RNUI.stopInteractionThreads()
		dpg.destroy_context()

