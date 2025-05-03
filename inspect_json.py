import json

# Open the large JSON file
with open('./data/kanjidata.json', 'r', encoding='utf-8') as f:
    # Load the entire JSON for inspection
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")
        exit()

# Inspect the 'kanjis' dictionary
if 'Kanji' in data:
    print("Inspecting 'kanjis':")
    kanjis = data['kanjis']
    # with open("/home/williamg/code/python/nihongone/data/kanjidata.json", 'w', encoding='utf-8') as json_file: 
    #     json.dump(kanjis, json_file, indent=4, ensure_ascii=False)
    if isinstance(kanjis, dict):
        print(f"'kanjis' contains {len(kanjis)} entries. First 3 entries:")
        count = 0
        for key, value in kanjis.items():
            print(f"  Key: {key}, Value: {json.dumps(value, indent=4, ensure_ascii=False)}")
            count += 1
            if count >= 3:
                break

# Similarly inspect 'readings' and 'words'
if 'readings' in data:
    print("\nInspecting 'readings':")
    readings = data['readings']
    if isinstance(readings, dict):
        print(f"'readings' contains {len(readings)} entries. First 3 entries:")
        count = 0
        for key, value in readings.items():
            print(f"  Key: {key}, Value: {json.dumps(value, indent=4, ensure_ascii=False)}")
            count += 1
            if count >= 3:
                break

if 'words' in data:
    print("\nInspecting 'words':")
    words = data['words']
    if isinstance(words, dict):
        print(f"'words' contains {len(words)} entries. First 3 entries:")
        count = 0
        for key, value in words.items():
            print(f"  Key: {key}, Value: {json.dumps(value, indent=4, ensure_ascii=False)}")
            count += 1
            if count >= 3:
                break

