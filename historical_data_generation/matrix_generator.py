import json
import math
import numpy as np
import pandas as pd

def generate_time_matrix(path,n):

    f = open(path)

    data = json.load(f)

    matrix = np.zeros((n+1, n+1), np.int8)

    i = 0
    for a in data['nodes']:
        if i > n:
            break
        j=0
        for b in data['nodes']:
            if j > n:
                break
            matrix[int(a['-id'])][int(b['-id'])] = int(round((math.sqrt((float(b['cx']) - float(a['cx']))**2
            + (float(b['cy']) - float(a['cy']))**2))/5))
            j += 1
        i += 1
    #nice = pd.DataFrame(matrix)
    #print(nice)
    return matrix.tolist()