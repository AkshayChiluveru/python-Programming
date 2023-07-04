import json

with open('json/states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], "--",state['area_codes'])