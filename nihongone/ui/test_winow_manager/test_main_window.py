# test_main_window.py
import urwid

class MainWindow:
    def __init__(self, manager):
        self.manager = manager
        self.main_menu = urwid.Text("""
Welcome!
1. Go to window 1
2. Go to window 2
""")
        self.main_frame = urwid.Filler(self.main_menu)

    def handle_input(self, key):
        if key == '1':
            self.manager.change_window(self.manager.window_1)
        elif key == '2':
            self.manager.change_window(self.manager.window_2)

