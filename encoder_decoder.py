""" This is the LSTM encoder-decoder architecture for number sorting.
- author: Suma Kori
- e-mail: suma.kori93@gmail.com
"""

# import necessary libraries
import random
import numpy as np
from numpy import array
from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from sklearn.metrics import mean_squared_error


def sort_random_numbers(examples, numbers, largest):

  """This method generate sequences of random integers and their sorted orders.
  Method takes the parameter example: specified number of examples,
  numbers:total number of integer in each sequence and largest integer to generate sequences

  :param: examples
  :type: int

  :param: numbers
  :type: int

  :param: largest
  :type: int

  """
  data, target = list(), list()
  for i in range(examples):
      unsorted = random.sample(range(1, largest), numbers)
      data.append(unsorted)
      print(unsorted, sorted(unsorted))
      target.append(sorted(unsorted))

  # normalize
  data = np.array(data, dtype=float)
  target = np.array(target, dtype=float)

  return data, target


# invert normalization
def invert(value, n_numbers, largest):
    return value * float(largest * n_numbers)


examples = 1000
numbers = 8
largest = 1000
# create LSTM
# Create a Keras model with the Sequential() constructor
model = Sequential()
model.add(LSTM(8, input_shape=(numbers, 1), return_sequences=True))
model.add(Dense(8))
model.compile(loss='mean_squared_error', optimizer='adam')
model.summary()

# train LSTM
data, target = sort_random_numbers(examples, numbers, largest)
data = data.reshape(examples, numbers, 1)
model.fit(data, target, epochs=5, batch_size=1, verbose=2)

# predict on new sequences
X, y = sort_random_numbers(examples, numbers, largest)
X = X.reshape(examples, numbers, 1)
predicted_sequence = model.predict(X, batch_size=1, verbose=0)

# calculate error
expected = [invert(x, numbers, largest) for x in y]
a = np.array(expected)
predicted = [invert(x, numbers, largest) for x in predicted_sequence[:, 1]]
b = np.array(predicted)
mses = ((b - a)**2).mean(axis=1)
print('error is ', mses)