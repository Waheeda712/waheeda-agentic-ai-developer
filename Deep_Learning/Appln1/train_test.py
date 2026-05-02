import numpy as np

import pandas as pd
# split data into train data and test data
from sklearn.model_selection import train_test_split
# Normalization
from sklearn.preprocessing import StandardScaler

from tensorflow import keras

import matplotlib.pyplot as plt
#Load Predefine data
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
print(data)
X = data.data # input data
y = data.target #Output data

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

#transform --> normalization
# fit --> allow model to learn pattern ex: y=2x, y=x*x

X_test = scaler.transform(X_test)

#here we are using only transorm because its a test data so need to allow learn the patterns alread it is learned in training state so now its test state so we use only transforms

model = keras.Sequential([
    keras.layers.Dense(32,activation='relu'),
    keras.layers.Dense(16,activation='relu'),
    keras.layers.Dense(1,activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss = 'binary_crossentropy',
    metrics = ['accuracy']
)

history = model.fit(X_train, y_train,epochs =100, validation_data =(X_test,y_test))

#history.history["accuracy"] --> traing(80%).plot
#history,history["val_accuracy"] --> test (20%) plot

if model.predict(X_test[0].reshape(1,-1))[0][0] > 0.5:
#X_test[0] is 1D array but in deeplearning we need 2D array so to maintain 1D to 2D array we use reshape
    print("Safe")
else:
    print("Danger")

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Train <> Test")
plt.legend(["Train" , "Test"])
plt.show()



