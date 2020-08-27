import requests
import json
import os
data = {
    'api_token': 'test',
    'return': 'apple_music,spotify',
}
files = {
    'file': open('clash.mp3', 'rb'),
}
result = requests.post('https://api.audd.io/', data=data, files=files)
jsonString=(result.text)
content = json.loads(jsonString)

data = {
    'api_token': 'test',
    'q': content["result"]["title"]+content["result"]["artist"],
}
res = requests.post('https://api.audd.io/findLyrics/', data=data)

ly=res.text

lyrics=json.loads(ly)


print(f"Artist :",content["result"]["artist"],"\n")
print(f"Title :",content["result"]["title"],"\n")
print(f"Album :",content["result"]["album"],"\n")
print(f"Lyrics :",lyrics["result"][0]["lyrics"])

os.startfile("clash.mp3")