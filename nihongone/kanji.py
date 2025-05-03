from typing import Optional, List

class Kanji:
    def __init__(self,
                 kanji: str,
                 strokes: Optional[int] = None,
                 grade: Optional[int] = None,
                 freq: Optional[int] = None,
                 jlpt_old: Optional[int] = None,
                 jlpt_new: Optional[int] = None,
                 meanings: Optional[List[str]] = None,
                 readings_on: Optional[List[str]] = None,
                 readings_kun: Optional[List[str]] = None,
                 wk_level: Optional[int] = None,
                 wk_meanings: Optional[List[str]] = None,
                 wk_readings_on: Optional[List[str]] = None,
                 wk_readings_kun: Optional[List[str]] = None,
                 wk_radicals: Optional[List[str]] = None,
                 examples: Optional[List[str]] = None):

        self.kanji = kanji  # The kanji character
        self.strokes = strokes  # Stroke count
        self.grade = grade  # Grade level (Kyōiku kanji or others)
        self.freq = freq  # Frequency rank
        self.jlpt_old = jlpt_old  # Old JLPT level
        self.jlpt_new = jlpt_new  # New JLPT level
        self.meanings = meanings or []  # English meanings (list)
        self.readings_on = readings_on or []  # On readings (list)
        self.readings_kun = readings_kun or []  # Kun readings (list)
        self.wk_level = wk_level  # WaniKani level
        self.wk_meanings = wk_meanings or []  # WaniKani meanings (list)
        self.wk_readings_on = wk_readings_on or []  # WaniKani On readings (list)
        self.wk_readings_kun = wk_readings_kun or []  # WaniKani Kun readings (list)
        self.wk_radicals = wk_radicals or []  # WaniKani radicals (list)
        self.examples = examples or [] #Example sentences for Kanji



    def just_the_kanji(self):
        return(
            f"Kanji: {self.kanji}\n"
        )

    def kanji_jlpt_freq(self):
        return(
            f"{self.kanji}, {self.jlpt_new}, {self.freq}"
        )


    def concise_info(self):
        return (
            f"Kanji: {self.kanji}\n"
            f"JLPT: {self.jlpt_new}\n"
            f"Meanings: {', '.join(self.meanings)}\n"
            f"On: {', '.join(self.readings_on)}\n"
            f"Kun: {', '.join(self.readings_kun)}\n"
            f"Examples: {', '.join(self.examples)}"
        )

    def detailed_info(self):
        """Returns a detailed string representation of the kanji's attributes."""
        return (
            f"Kanji: {self.kanji}\n"
            f"Strokes: {self.strokes}\n"
            f"Grade: {self.grade}\n"
            f"Frequency: {self.freq}\n"
            f"JLPT (Old): {self.jlpt_old}\n"
            f"JLPT (New): {self.jlpt_new}\n"
            f"Meanings: {', '.join(self.meanings)}\n"
            f"On Readings: {', '.join(self.readings_on)}\n"
            f"Kun Readings: {', '.join(self.readings_kun)}\n"
            f"WaniKani Level: {self.wk_level}\n"
            f"WaniKani Meanings: {', '.join(self.wk_meanings)}\n"
            f"WaniKani On Readings: {', '.join(self.wk_readings_on)}\n"
            f"WaniKani Kun Readings: {', '.join(self.wk_readings_kun)}\n"
            f"WaniKani Radicals: {', '.join(self.wk_radicals)}\n"
            f"Examples: {', '.join(self.examples)}"
        )

