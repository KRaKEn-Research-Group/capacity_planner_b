import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sklearn.metrics import classification_report, confusion_matrix
from historical_data_generation.demand_generator import weather_quality
from solver.solver import solve_date
import csv
import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt  
from sklearn.datasets import make_classification
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error

def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

def prepare_inputs(X_train, X_test):
	oe = OrdinalEncoder()
	oe.fit(X_train)
	X_train_enc = oe.transform(X_train)
	X_test_enc = oe.transform(X_test)
	return X_train_enc, X_test_enc

generate_file = False

if generate_file:
    n_days = 5000
    y=np.zeros(n_days)
    x=np.zeros((n_days,3))
    with open("data/in/weather_data.csv") as csvfile:
        # num of days
        i=0
        for row in csv.reader(csvfile, delimiter=','):
            print(i)
            if i==0:
                i +=1
                continue
            day = datetime.datetime(int(row[0]),int(row[1]),int(row[2])).weekday()
            y[i-1] = solve_date((row[0], row[1], row[2]),100)
            x[i-1][0] = int(row[1])
            x[i-1][1] = int(row[2])
            x[i-1][2] = day
            i += 1
            if i == n_days+1:
                break
        res = np.append(x, y.reshape(n_days,1), axis=1)
        pd.DataFrame(res).to_csv("data/out/network_data5.csv")

    print(x)
    print(y)

#for i in weather
# i znowu for na x z data
# nie wiem czy moze byc dwukolumnowy
# ale wtedy na druga kolumne for z pogoda
else:
    data = pd.read_csv("data/out/network_data_glued.csv")
    data.pop('RECORD')
    #data.pop('RECORD2')
    data.pop('DAY')
    data.pop('year')
    data.pop('mo')
    data.pop('da')
    data.pop('prcp')
    #data.pop('MONTH')
    
    y = data.values[:, -1] 
    x = data.values[:, :-1]

    #plt.plot(range(len(y)),y)
    #plt.show()
    #print(x)
    #print(y)
    x = x.astype('int64')
    x = x.astype('str')
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

    X_train, X_test = prepare_inputs(X_train, X_test)
    print("Train length: ", len(X_train))
    print("Test length: ", len(X_test))

    model = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(32, 16, 16), random_state=1, activation = "relu", max_iter = 200, n_iter_no_change=50, batch_size=10, verbose = True)
    #model = LogisticRegression()
    model.fit(X_train,y_train)

    print("PREDICTED")
    print(model.predict(X_test))
    print("REAL")
    print(y_test)
    print("Probability")
    print(model.predict_proba(X_test))

    print("TRAINING DATA")
    print("Score: ",model.score(X_train,y_train))
    print("MSE: ",mean_squared_error(y_train,model.predict(X_train)))


    print("TESTING DATA")
    print("Score: ",model.score(X_test,y_test))
    print("MSE: ",mean_squared_error(y_test,model.predict(X_test)))

    #plot_confusion_matrix(model, X_test, y_test)  
    #plt.show()  