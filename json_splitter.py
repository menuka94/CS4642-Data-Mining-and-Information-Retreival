import json
import os

with open('data.json') as f:
    data = json.load(f)

i = 1
for record in data:
    filename = os.path.join("jsonFiles", str(i) + ".json")
    f = open(filename, 'w+')
    json.dump(record, f)
    f.flush()
    f.close()
    i += 1
