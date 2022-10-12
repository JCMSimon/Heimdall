import dearpygui.dearpygui as dpg
from screeninfo import get_monitors
# from lib.Logger import Logger

class Loader:
	def __init__(self) -> None:
		# self.logger = Logger
		self.initDPG()
		self.initMainWindow()
		self.start()

	def initDPG(self):
		dpg.create_context()
		with dpg.texture_registry():
			self.width, self.height, _, data = dpg.load_image("./assets/heimdall_logo.png")
			self.Image = dpg.add_dynamic_texture(self.width, self.height, data,tag="test")
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
		self.centerViewport()

	def centerViewport(self):
		for monitor in get_monitors():
			if monitor.is_primary:
				monitor_xd = monitor.width
				monitor_yd = monitor.height
		dpg.set_viewport_pos([
			int(monitor_xd + self.width / 2),
			int(monitor_yd + self.height / 2)
			]
		)

	def initMainWindow(self):
		# Main Window (Wrapper)
		with dpg.window(
			tag="mainWindow",
			horizontal_scrollbar=False,
			no_background=False,
			no_scrollbar=True,
			no_title_bar=True,
			no_collapse=True,
			no_resize=True,
			menubar=False,
			no_close=True,
			no_move=True,

			):
			dpg.add_image(texture_tag="test",width=100,height=100)
		dpg.set_primary_window("mainWindow",True)
		print(dpg.get_viewport_pos())


	# Starts GUI
	def start(self):
		dpg.start_dearpygui()

if __name__ == "__main__":
	_ = Loader()