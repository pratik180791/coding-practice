output = [{"Aisle name": "Canned and Jarred", "Amount": "2.0$", "Name": "beef broth", "Unit": "cups"}, {"Aisle name": "Meat", "Amount": "1.0$", "Name": "pork tenderloin", "Unit": "serving"}]


def get_random():
    return 1

a = [get_random() for i in range(3)]
print(a)

import json
import ast
import pandas as pd
output = json.dumps(output)
val = ast.literal_eval(output)
val1 = json.loads(json.dumps(val))
# val2 = val1['tags'][0]['results'][0]['values']
pd.set_option('colheader_justify', 'right')
val1 = pd.DataFrame(val1)
print(val1.to_markdown())

