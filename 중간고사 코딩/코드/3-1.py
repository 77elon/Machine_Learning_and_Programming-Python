import tensorflow as tf
from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images.shape

len(train_labels)

len(test_labels)

digit = train_images[4]

import matplotlib.pyplot as plt

plt.imshow(digit, cmap = plt.cm.binary)

plt.savefig('result.png')
