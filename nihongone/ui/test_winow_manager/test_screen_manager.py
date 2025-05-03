# screen_manager.py
import urwid
import test_main_window
import test_window_1
import test_window_2

class ScreenManager:
    def __init__(self):
        self.main_window = test_main_window.MainWindow(self)
        self.window_1 = test_window_1.Window1(self)
        self.window_2 = test_window_2.Window2(self)
        self.current_window = self.main_window

    def handle_input(self, key):
        self.current_window.handle_input(key)

    def change_window(self, window):
        self.current_window = window
        self.loop.widget = window.main_frame

    def start(self):
        self.loop = urwid.MainLoop(self.current_window.main_frame, unhandled_input=self.handle_input)
        self.loop.run()

if __name__ == "__main__":
    manager = ScreenManager()
    manager.start()

