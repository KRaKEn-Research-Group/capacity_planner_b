import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


# for i in date:
#     y.append(solve_date(date,100))

#y.reshape(-1,1)

#for i in weather
# i znowu for na x z data
# nie wiem czy moze byc dwukolumnowy
# ale wtedy na druga kolumne for z pogoda



model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x,y)