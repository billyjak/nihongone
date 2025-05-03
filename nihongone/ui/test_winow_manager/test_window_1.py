# test_window_1.py
import urwid

class Window1:
    def __init__(self, manager):
        self.manager = manager
        self.window1_text = urwid.Text("""
Welcome to Window 1!
B. Go back
2. Go to Window 2
""")
        self.main_frame = urwid.Filler(self.window1_text)

    def handle_input(self, key):
        if key == 'b' or key == 'B':
            self.manager.change_window(self.manager.main_window)
        elif key == '2':
            self.manager.change_window(self.manager.window_2)

