import dearpygui.dearpygui as dpg
from lib.Logger import Logger

class GUI:
	def __init__(self) -> None:
		# Gui-Config ##########
		self.width,self.height = 1080,720
		# plugin Stuff ########
		#TODO Init Plugin Handler here
		# Gui Stuff ###########
		self.logger = Logger("GUI")
		self.debug = True
		dpg.create_context()
		dpg.create_viewport(
			clear_color=(111,111,111,255),
			vsync=True,
			resizable=False,
			decorated=False,
			height=self.height,
			width=self.width,
			title="Heimdall",
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		self.initMainWindow()
		self.start()

	def initMainWindow(self):
		with dpg.font_registry():
			titleFont = dpg.add_font("assets/Cousine-Regular.ttf", 25)
			searchFont = dpg.add_font("assets/Cousine-Regular.ttf", 20)
		#Main Window (Wrapper)
		with dpg.window(horizontal_scrollbar=False, no_background=True ,no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=True, no_close=True, no_move=True, tag="mainWindow") as mainWindow:
			# Make dragging the Window possible
			with dpg.handler_registry():
				dpg.add_mouse_drag_handler(button=0, threshold=0.0, callback=self.drag)
			#style Window
			with dpg.theme() as mainWindowStyling:
				with dpg.theme_component(dpg.mvAll):
					dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive,(90,0,170,100))
					dpg.add_theme_color(dpg.mvThemeCol_TitleBg,(90,0,170,100))
					dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed,(90,0,170,100))
					dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(255,0,0,100))
					dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(255,0,0,255))
					dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign,0.5,0.5)
					dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
					dpg.bind_theme(mainWindowStyling)
					dpg.bind_font(titleFont)


			#Node Editor Window
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=False, no_move=True, height = int(self.height / 100 * 80), width=self.width, tag="nodeWindow", label="Heimdall", on_close=self.exit):
				self.nodeUI = dpg.add_node_editor(
					minimap=True,
					minimap_location=dpg.mvNodeMiniMap_Location_TopLeft
				)

			#Search Window
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=False, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=True, no_move=True, height=int(self.height / 100 * 20), width=self.width, tag="searchWindow", label="Search", pos = [0, int(self.height / 100 * 80)]) as searchWindow:
				dpg.bind_item_font(searchWindow,searchFont)

				# Button to Choose what to search for
				self.typeSelector = dpg.add_combo(default_value=padItems(["Username","z"])[1], no_arrow_button=True, tag="sea rchGuiTypeSelector", width=int(self.width / 100 * 95), pos = [int(self.width / 2) - int(int(self.width / 100 * 95) / 2),int(int(int(self.height / 100 * 20) / 100 * 80) - 27)],
					items=padItems(["Email", "Image", "Name", "Phone Number", "Username"]))
				# Search Bar for input
				self.searchBar = dpg.add_input_text(pos = [int(self.width / 2) - int(int(self.width / 100 * 95) / 2),int(int(int(self.height / 100 * 20) / 100 * 50) - 27)], width=int(self.width / 100 * 95) - 70, hint="Search here...")
				# Buttont to submit search
				self.submitButton = dpg.add_button(label="Submit", pos = [int(self.width / 2) - int(int(self.width / 100 * 95) / 2) + int(int(self.width / 100 * 95) - 70) - 4 ,int(int(int(self.height / 100 * 20) / 100 * 50) - 27)]
				)
				with dpg.theme() as submitButton:
					with dpg.theme_component(dpg.mvAll):
						dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered,(0,255,0,100))
						dpg.add_theme_color(dpg.mvThemeCol_ButtonActive,(0,255,0,255))
						dpg.bind_item_theme(self.submitButton,submitButton)

		dpg.set_primary_window("mainWindow", True)


	def addNode(text):#prob more stuff
		pass

	def removeNode(node):
		pass


	def start(self):
		dpg.start_dearpygui()

	def exit(self):
		dpg.destroy_context()

	#Thanks to https://github.com/bandit-masked
	def drag(self,sender, app_data, user_data):
		if dpg.get_mouse_pos(local=False)[1] < 40:  # only drag the viewport when dragging the logo
			drag_deltas = app_data
			viewport_current_pos = dpg.get_viewport_pos()
			new_x_position = viewport_current_pos[0] + drag_deltas[1]
			new_y_position = viewport_current_pos[1] + drag_deltas[2]
			new_y_position = max(new_y_position, 0) # prevent the viewport to go off the top of the screen
			dpg.set_viewport_pos([new_x_position, new_y_position])

def padItems(itemList) -> list:
	itemList.sort(key=len)
	newItemList = []
	for item in itemList: #what the fuck is this stuff to make text centered omg xd
		tempItem = item
		while len(tempItem) != 92:
			if len(tempItem) %2 == 0:
				tempItem = tempItem+" "
			else:
				tempItem = " "+tempItem
		newItemList.append(tempItem)
	return newItemList

if __name__ == "__main__":
	Heimdall = GUI()



