import urwid
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from nihongone.kanji_manager import KanjiManager

class KanjiSearchApp:
    def __init__(self):
        self.manager = KanjiManager()
        self.prompt = urwid.Text("Kanji Search\n")
        self.input_edit = urwid.Edit("Enter meaning: ")
        self.results = urwid.Text("")
        self.layout = urwid.Pile([self.prompt, self.input_edit, self.results])
        self.fill = urwid.Filler(self.layout)
        self.loop = urwid.MainLoop(self.fill, unhandled_input=self.handle_input)

    def handle_input(self, key):
        if key == 'enter':
            user_input = self.input_edit.edit_text.strip()
            if user_input:
                kanji_list = self.manager.filter_kanji(meanings=user_input)
                kanji_info = "\n\n".join(kanji.concise_info() for kanji in kanji_list)
                self.results.set_text(kanji_info)
            else:
                self.results.set_text("")
            self.input_edit.set_edit_text("")

    def run(self):
        self.loop.run()

if __name__ == "__main__":
    app = KanjiSearchApp()
    app.run()

