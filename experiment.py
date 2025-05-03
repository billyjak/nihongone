from nihongone.kanji_manager import KanjiManager

kanji_list = KanjiManager("./data/davidluzgouveia_kanji_database/kanjiapi_full.json")
missing_freq = [
    kanji for kanji, attributes in kanji_list.items()
    if attributes.get('jlpt_new') in range(1, 6) and attributes.get('freq') is None
]

if missing_freq:
    print(f"Number of kanji in JLPT levels 1-5 without freq: {len(missing_freq)}")
    print("Examples:", missing_freq)  # Show the first 5 kanji missing freq for reference
else:
    print("All kanji in JLPT levels 1-5 have a freq value.")

# new_list = kanji_list.filter_kanji(freq=1)
# print("something is working")
# for kanji_obj in new_list:
#     print(kanji_obj.kanji)
