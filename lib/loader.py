import dearpygui.dearpygui as dpg
from screeninfo import get_monitors
from lib.temp.windows import set_transparent_color
# from lib.Logger import Logger

class Loader:
	def __init__(self) -> None:
		# self.logger = Logger
		self.initDPG()
		self.initDPGThemes()
		self.initMainWindow()
		self.start()

	def initDPG(self):
		dpg.create_context()
		with dpg.texture_registry():
			self.width, self.height, _, data = dpg.load_image("./assets/heimdall_logo.png")
			self.Image = dpg.add_dynamic_texture(self.width, self.height, data,tag="logo")
		dpg.create_viewport(
			title="Heimdall",              # Window Title (Also Application Title)
			large_icon="assets/icon.ico",  # "favicon" for Application
			small_icon="assets/icon.ico",  # "favicon" for Application
			decorated=False,               # Disables Windows Bar
			resizable=False,
			height=self.height,
			width=self.width,
			x_pos = -self.width,
			y_pos = -self.height,
			)
		dpg.setup_dearpygui()
		dpg.show_viewport()
		#Thanks to https://github.com/Atlamillias for this temporary workaround
		set_transparent_color((0,0,0))
		self.centerViewport()

	def centerViewport(self):
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos(pos=[
			(monitor_xd - self.width) / 2,
			(monitor_yd - self.height) / 2,
		])

	def initDPGThemes(self):
		with dpg.theme() as mainWindowStyling:
			with dpg.theme_component(dpg.mvAll):
				dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize,0)
				dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,0,0)
				dpg.add_theme_color(dpg.mvThemeCol_WindowBg,(0,0,0))
				dpg.bind_theme(mainWindowStyling)

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
			dpg.add_image(texture_tag="logo",width=self.width,height=self.height)
		dpg.set_primary_window("mainWindow",True)
		dpg.show_style_editor()

	# Starts GUI
	def start(self):
		dpg.start_dearpygui()

if __name__ == "__main__":
	_ = Loader()