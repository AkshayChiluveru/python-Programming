import json

# with open('json/states.json') as f:
#     data = json.load(f)

# for state in data['states']:
#     print(state['name'], "--",state['area_codes'])




# deleting and creating a new file:

with open('json/states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_codes']

with open('json/new_states.json', 'w') as f:
    json.dump(data, f, indent=4)

