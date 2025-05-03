# test_window_2.py
import urwid

class Window2:
    def __init__(self, manager):
        self.manager = manager
        self.window2_text = urwid.Text("""
Welcome to Window 2!
B. Go back
1. Go to Window 1
""")
        self.main_frame = urwid.Filler(self.window2_text)

    def handle_input(self, key):
        if key == 'b' or key == 'B':
            self.manager.change_window(self.manager.main_window)
        elif key == '1':
            self.manager.change_window(self.manager.window_1)

