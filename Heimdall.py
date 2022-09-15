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
			titleFont = dpg.add_font("assets/Arial.ttf", 25)
			searchFont = dpg.add_font("assets/Arial.ttf", 20)
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
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=False, no_move=True, height = int(self.height / 100 * 65), width=self.width - 15, tag="nodeWindow", label="Heimdall", on_close=self.exit):
				pass

			#Search Window
			with dpg.window(horizontal_scrollbar=False, no_scrollbar=True, no_collapse=True, no_resize=True, menubar=False, no_title_bar=False, no_close=True, no_move=True, height = int(self.height / 100 * 35), width=self.width - 15, tag="searchWindow", label="Search", pos = [0, int(self.height / 100 * 65)]) as searchWindow:
				dpg.bind_item_font(searchWindow,searchFont)
				self.typeSelector = dpg.add_combo(default_value="Username", no_arrow_button=True, tag="searchGuiTypeSelector", width=self.width - 40,
					items=("Email", "Image", "Name", "Phone Number", "Username", "Username", "Username", "Username", "Username", "Username",),)
				pass
		dpg.set_primary_window("mainWindow", True)


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

Heimdall = GUI()

