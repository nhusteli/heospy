import json
import pprint

f = open('response.txt', 'r')
response = f.read()
f.close()
response = json.loads(response)
pprint.pprint(response)
print(response["payload"][0]["name"])