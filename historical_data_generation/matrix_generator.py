import json
import math
import numpy as np
import pandas as pd

def generate_time_matrix(path):

    f = open(path)

    data = json.load(f)

    matrix = np.zeros((201, 201), np.int8)

    for a in data['nodes']:
        for b in data['nodes']:
            matrix[int(a['-id'])][int(b['-id'])] = int((math.sqrt((float(b['cx']) - float(a['cx']))**2
            + (float(b['cy']) - float(a['cy']))**2))/30)


    #nice = pd.DataFrame(matrix)
    #print(nice)
    return matrix.tolist()