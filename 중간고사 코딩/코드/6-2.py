import tensorflow as tf
import numpy as np

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], 'float32')
y = np.array([[0], [0], [0], [1]], 'float32')
#y = np.array([[0], [1], [1], [1]], 'float32')
#y = np.array([[0], [1], [1], [0]], 'float32')

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(2, input_dim = 2, activation ="sigmoid"))
model.add(tf.keras.layers.Dense(1))

sgd = tf.keras.optimizers.SGD(learning_rate = 0.01, momentum = 0.97)
model.compile(optimizer = sgd, loss='mean_squared_error')

hist = model.fit(x, y, epochs=1000, batch_size = 1, verbose = 0)

model.summary()
print(model.predict(x))

#matplotlib inline
import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label = 'train loss')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
loss_ax.legend(loc='upper left')
