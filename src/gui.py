import time
import dearpygui.dearpygui as dpg

from src._Logger import Logger
class GUI:
	def __init__(self,debug=False) -> None:
		self.logger = Logger("GUI",debug=debug)
		self.width,self.height = 1080,720
		self.initDPG()
		self.initDPGThemes()
		self.initMainWindow()

	def returnEditor(self):
		return self.nodeInterface

	def initDPG(self):
		dpg.create_context()
		dpg.create_viewport(
			title="Heimdall",              # Window Title (Also Application Title)
			clear_color=(111,111,111,255), # Background Color
			large_icon="assets/icon.ico",  # "favicon" for Application
			small_icon="assets/icon.ico",  # "favicon" for Application
			decorated=False,               # Disables Windows Bar
			resizable=False,
			vsync=True,
			height=self.height,
			width=self.width,
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()

	def initDPGThemes(self):
		with dpg.font_registry():
			self.titleFont = dpg.add_font("assets/Cousine-Regular.ttf", 25)
			self.searchFont = dpg.add_font("assets/Cousine-Regular.ttf", 20)
		with dpg.theme() as mainWindowStyling:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
				dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed,(90,0,170,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(255,0,0,100))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255,0,0,255))
				dpg.bind_theme(mainWindowStyling)
				dpg.bind_font(self.titleFont)
		with dpg.theme() as self.submitButtonTheme:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(120,0,200,255))
				dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered,(90,0,170,255))
				dpg.add_theme_color(dpg.mvThemeCol_HeaderActive,(120,0,200,255))

	def initMainWindow(self):
		# Main Window (Wrapper)
		with dpg.window(
			tag="mainWindow",
			horizontal_scrollbar=False,
			no_background=True,
			no_scrollbar=True,
			no_title_bar=True,
			no_collapse=True,
			no_resize=True,
			menubar=False,
			no_close=True,
			no_move=True,
			):
			with dpg.handler_registry():   # Make dragging the Window possible
				dpg.add_mouse_drag_handler(
					callback=self.dragWindow,
					threshold=0.0,
					button=0,
					)
			# Node Editor Window (Wrapper)
			with dpg.window(
				tag="nodeWindow",
				label="Heimdall",          # This defines the actual title of the Application
				on_close=self.exitGUI,
				horizontal_scrollbar=False,
				no_title_bar=False,
				no_scrollbar=True,
				no_collapse=True,
				no_close=False,
				no_resize=True,
				menubar=False,
				no_move=True,
				height = int(self.height / 100 * 80), # Make it take up 80% of the Window Height
				width=self.width,
				):
				# Node Editor (VIS)
				self.nodeUI = dpg.add_node_editor(
					minimap=True,
					minimap_location=dpg.mvNodeMiniMap_Location_TopLeft
				)
			#Search Window
			with dpg.window(
				tag="searchWindow",
				label="Search",
				horizontal_scrollbar=False,
				no_title_bar=False,
				no_scrollbar=False,
				no_collapse=True,
				no_resize=True,
				menubar=False,
				no_close=True,
				no_move=True,
				width=self.width,
				height=int(self.height / 100 * 20),
				pos = [
					0,                                # x Axis
					int(self.height / 100 * 80)       # y Axis
					],
				) as searchWindow:
				dpg.bind_item_font(searchWindow,self.searchFont)
				# Button to Choose what to search for (Type Selector Button)
				self.logger.debugMsg(f"Plugin Names before padding: {self.plReg.getPluginNames()}")
				self.typeSelector = dpg.add_combo(
					tag="searchGuiTypeSelector",
					# REPLACE WITH CORE
					items=centerText(self.plReg.getPluginNames()), #["Email", "Image", "Name", "Phone Number", "Username"]
					# REPLACE WITH CORE
					default_value=centerText("Username"),
					callback=self.typeSelectorCallback,
					no_arrow_button=True,
					width=int(self.width / 100 * 95),
					pos = [
						int(self.width / 2) - int(int(self.width / 100 * 95) / 2), # x Axis
						int(int(int(self.height / 100 * 20) / 100 * 80) - 27)],    # y axis
					)
				self.logger.debugMsg(f"Plugin Names after padding:")
				# REPLACE WITH CORE
				for name in centerText(self.plReg.getPluginNames()):
				# REPLACE WITH CORE
					self.logger.debugMsg(f"{name}(EOL)")
				self.dataType = "Username"
				dpg.bind_item_theme(self.typeSelector,self.submitButtonTheme)
				# Search Bar for input
				self.searchBar = dpg.add_input_text(
					hint="Search here...",            # Text that is in the Box when nothing is typed
					on_enter=True,
					callback=self.searchBarCallback,
					width=int(self.width / 100 * 95) - 70,
					pos = [
						int(self.width / 2) - int(int(self.width / 100 * 95) / 2),
						int(int(int(self.height / 100 * 20) / 100 * 50) - 27)
						],
					)
				# Buttont to submit search
				self.submitButton = dpg.add_button(
					label="Submit",                   # Button Text
					callback=self.searchButtonCallback,
					pos = [
						int(self.width / 2) - int(int(self.width / 100 * 95) / 2) + int(int(self.width / 100 * 95) - 70) - 4 , # x Axis
						int(int(int(self.height / 100 * 20) / 100 * 50) - 27)]                                                 # y Axis
				)
				dpg.bind_item_theme(self.submitButton,self.submitButtonTheme)
		dpg.set_primary_window("mainWindow", True)    # Maximize the Main Window Wrapper

	# Gets called when a option is selected
	def typeSelectorCallback(self, _, app_data):
		self.dataType = str(app_data).strip()
		self.logger.debugMsg(f"Selected '{self.dataType}' as data type")

	# Gets called when the "Submit" Button gets called
	# Forwards to searchBarCallback
	def searchButtonCallback(self, _, __):
		searchTerm = dpg.get_value(self.searchBar)
		self.searchBarCallback("Manual",searchTerm)

	# Gets called when Enter is pressed in the Searchbar
	def searchBarCallback(self, _, app_data):
		searchTerm = str(app_data).strip()
		if searchTerm and searchTerm != "":
			dpg.disable_item(self.searchBar)
			dpg.disable_item(self.submitButton)
			dpg.set_value(self.searchBar,f"Processing '{searchTerm}' as {self.dataType}...")
			self.logger.debugMsg(f"Processing Search Term: '{searchTerm}' ")
			self.executeSearch(searchTerm)
			dpg.set_value(self.searchBar,"")
			dpg.enable_item(self.searchBar)
			dpg.enable_item(self.submitButton)

	def executeSearch(self,searchTerm):
		# REPLACE WITH CORE
		data = self.plReg.runPlugin(self.dataType,searchTerm)
		# REPLACE WITH CORE
		return data

	# Starts GUI
	def start(self,core):
		self.core = core
		dpg.start_dearpygui()

	# End GUI
	def exitGUI(self):
		dpg.destroy_context()

	# Function to handle dragging the Window
	# Thanks to https://github.com/bandit-masked
	def dragWindow(self,sender, app_data, user_data):
		if dpg.get_mouse_pos(local=False)[1] < 40:  # only drag the viewport when dragging the logo
			drag_deltas = app_data
			if drag_deltas[0] != 0 or drag_deltas[1] != 0:
				viewport_current_pos = dpg.get_viewport_pos()
				new_x_position = viewport_current_pos[0] + drag_deltas[1]
				new_y_position = viewport_current_pos[1] + drag_deltas[2]
				new_y_position = max(new_y_position, 0) # prevent the viewport to go off the top of the screen
				self.logger.debugMsg(f"Moving Window to x:{new_x_position} y:{new_y_position} (Delta: {drag_deltas}")
				dpg.set_viewport_pos([new_x_position, new_y_position])
			else:
				return

# Used to center text in typeSelector
def centerText(itemList):
	if type(itemList) == str:
		while len(itemList) != 92:
			itemList = f"{itemList:^92}"
		return str(itemList)
	elif type(itemList) == list:
		# Sort List
		itemList.sort(key=len)
		newItemList = []
		for item in itemList: #what the fuck is this stuff to make text centered omg xd
			tempItem = item
			while len(tempItem) != 92: # Gui element has space for 92 chars
				tempItem = f"{tempItem:^92}"
			newItemList.append(tempItem)
		return list(newItemList)