import requests
import json, os

directory = "emojis"
curr_path = os.getcwd()
path = os.path.join(curr_path, directory)

# Create emojis directory if it doesn't already exist
try:
    os.mkdir(path)
except:
    print(f"folder {directory} already made")

# write each emoji found in emojis.json to the /emojis folder
with open('emojis.json', 'r') as f:
    emojilist = json.load(f)
for name in emojilist:
    url = emojilist[name]
    if url[:5] == "https":
        r = requests.get(url)
        with open(path + "/" + name + url[-4:], 'wb') as f:
            f.write(r.content)
            print("Added file " + name + url[-4:])
    elif url[:5] == "alias":
        actual_name = url[6:]
        try:
            actual_url = emojilist[actual_name]
        except KeyError as e:
            continue
        r = requests.get(actual_url)
        with open(path + "/" + name + actual_url[-4:], 'wb') as f:
            f.write(r.content)
            print("Added file " + name + actual_url[-4:])
