import os
import json
import time

exists = os.path.exists("./database.json")
if not exists:
    with open("./database.json", "w", encoding="utf-8") as f:
        f.write("[]")

while True:
    action = input("Choose your action (\"New\", \"Export\", \"Stat\")\n>>> ")
    if action.lower() == "new":
        while True:
            print()
            q = input("Write the question (Write \"Back\" for main menu)\n>>> ")
            if q.lower() == "back":
                break
            co = input("A. Correct Option (Answer)\n>>> ")
            o2 = input("B. Option 2\n>>> ")
            o3 = input("C. Option 3\n>>> ")
            o4 = input("D. Option 4\n>>> ")

            with open("./database.json", "r", encoding="utf-8") as f:
                data = json.load(f)
            data.append({
                "question": q,
                "options": [co, o2, o3, o4],
                "correct": co
            })
            
            with open("./database.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
    elif action.lower() == "export":
        with open("./database.json", "r", encoding="utf-8") as f:
            d = json.load(f)

        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        tmstmp = int(time.time())
        with open(f"{desktop}/database_{tmstmp}.json", "w", encoding="utf-8") as f:
            json.dump(d, f, indent=4, ensure_ascii=False)

        os.popen(f"{desktop}/database_{tmstmp}.json")

    elif action.lower() == "stat":
        with open("./database.json", "r", encoding="utf-8") as f:
            d = json.load(f)

        print(f"<<<<| Questions in Local Database: {len(d)} |>>>>")
    else:
        print("Invalid Action!")
    print()