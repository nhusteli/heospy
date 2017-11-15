import json
import pprint

f = open('response.txt', 'r')
response = json.loads(f.read())
f.close()
pprint.pprint(response)
print(response["payload"][0]["name"])