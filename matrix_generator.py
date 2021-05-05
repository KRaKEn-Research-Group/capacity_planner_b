import json
import math
import numpy as np
import pandas as pd

f = open("nodes.json")

data = json.load(f)

matrix = np.zeros((201,201))

for a in data['nodes']:
    for b in data['nodes']:
        matrix[int(a['-id'])][int(b['-id'])] = math.sqrt((float(b['cx']) - float(a['cx']))**2 
        + (float(b['cy']) - float(a['cy']))**2)

nice = pd.DataFrame(matrix)
print(nice)