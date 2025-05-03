import unittest
from nihongone.kanji_manager import KanjiManager

class TestKanjiManager(unittest.TestCase):
    def setUp(self):
        self.kanji_manager = KanjiManager("../data/kanjiapi_full.json")

    def test_jlpt_level_4_kanji(self):
        jlpt_4_kanji = self.kanji_manager.filter_kanji(jlpt=4)
        kanji_list = [kanji.kanji for kanji in jlpt_4_kanji]
        print(kanji_list)


if __name__ == "__main__":
    unittest.main()
