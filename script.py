import requests
import json

with open('emojis.json', 'r') as f:
    emojilist = json.load(f)
for name in emojilist:
    url = emojilist[name]
    if url[:5] == "https":
        r = requests.get(url)
        with open(name + url[-4:], 'wb') as f:
            f.write(r.content)
            print("Added file " + name + url[-4:])
    elif url[:5] == "alias":
        actual_name = url[6:]
        try:
            actual_url = emojilist[actual_name]
        except KeyError as e:
            continue
        r = requests.get(actual_url)
        with open(name + actual_url[-4:], 'wb') as f:
            f.write(r.content)
            print("Added file " + name + actual_url[-4:])%