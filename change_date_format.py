import json
import os
from datetime import datetime

with open('data.json') as f:
    data = json.load(f)

i = 1
for record in data:
    current_date = record['date_published']
    record['date_published'] = datetime.strptime(current_date, "%B %d, %Y").isoformat()
    i += 1

f = open("news1.json", 'w+')
json.dump(data, f)
f.flush()
f.close()
