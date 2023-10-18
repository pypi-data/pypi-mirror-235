import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
from skynet_ml.nn.models import Sequential
from skynet_ml.nn.losses import CategoricalCrossEntropy, BinaryCrossEntropy
from skynet_ml.metrics import ConfusionMatrix
from skynet_ml.nn.regularizers import L2
from skynet_ml.utils import EarlyStopping
from skynet_ml.nn.optimizers import Adam, SGD, AdaGrad, RMSProp
from skynet_ml.nn.layers import Dense
from skynet_ml.utils import save_model, plot_model, plot_training_history

(x_train, y_train), (x_test, y_test) = mnist.load_data()
num_labels = len(np.unique(y_train))
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
image_size = x_train.shape[1]
input_size = image_size**2

x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

model = Sequential()
model.add(Dense(16, activation="leaky_relu", input_dim=input_size))
model.add(Dense(16, activation="leaky_relu"))
model.add(Dense(num_labels, activation="linear", initializer="he_normal"))
model.compile(optimizer=Adam(learning_rate=0.001), loss=CategoricalCrossEntropy(from_logits=True), regularizer=L2())

model.fit(
    x_train=x_train,
    y_train=y_train,
    x_val=x_test,
    y_val=y_test,
    epochs=30,
    batch_size=64,
    early_stopping=EarlyStopping(patience=5, min_delta=0.0001)
)

evaluation = model.evaluate(x_test, y_test)
print(evaluation)