# tensorflow -- Deep Learning Library (engine)
import tensorflow as tf

#keras -- used to build deep Learning "Model" (Steering)
import tensorflow as keras

#numpy used to work with lists
import numpy as np

#input -- deeplearning takes input in the form 2D its a library standards
x = np.array([[1],[2],[3],[4]])

#output data -- deeplearning will learn throught the data provided
y = np.array([[1],[4],[9],[16]])


# Model -- we create the model with the help of Keras
# here we use sequential predifine function because deep learning uses sequential pattern of neutrons 
#keras.layers.Dense(3,activation='relu'),keras.layers.Dense(1)) this line explains that no.of sequencial neuroal network here we take 3 for input and activation is used "relu" 
#is nothing but to remove the (error) negative vaules and for output we use 1 neuron for output

# model = keras.Sequential(keras.layers.Dense(3,activation='relu'),
#                          keras.layers.Dense(1))

from tensorflow import keras

model = keras.models.Sequential([
    keras.layers.Dense(3, activation='relu'),
    keras.layers.Dense(1)
])

#Compile -- adam is used for adjusted the weights to reduced the mean_squared_error in weights

model.compile(
    optimizer = 'adam',
    loss = 'mean_squared_error'
)

# Train the model
#epochs is used for train the data "n" number of times like here we are train it 500 times

model.fit(x,y, epochs =500)

#predict
# here we are hardcoded the value for practrice 
# we need to get the data from API's Dynamically
# we need to get the data from java/reactjs/angular/ js/ 
# TO expose API's we need Fast API
# TO expose(run) server we need lightweight server called UVicorn server
print(model.predict(np.array([[5]])))