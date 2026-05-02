# import requroed libraries

import tensorflow as tf
from tensorflow import keras
import numpy as np

from fastapi import FastAPI


# Schema is nothing defining data type
# #Base model is used to define schema  
from pydantic import BaseModel


#input and output is in the form or array 
# we use list array here


x = np.array([[1],[2],[3],[4]])# input 
#operation x*x =y
y = np.array([[1],[4],[9],[16]]) # output

#create model

model = keras.models.Sequential([
    keras.layers.Dense(3, activation='relu'),
    keras.layers.Dense(1)
])

#Compile

model.compile(
    optimizer = 'adam',
    loss = 'mean_squared_error'
)


#Train the model
model.fit(x,y, epochs = 500)

app =FastAPI()

class TestData(BaseModel):
    num : float

@app.get("/")
def home():
    return {"message" : "welcome to FastAPT !!!"}

@app.post("/predict")
def predict(obj: TestData):
    res = model.predict(np.array([[obj.num]]))
    return {"result": float(res[0][0])}
#pridect

