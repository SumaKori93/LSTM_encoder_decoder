# LSTM encoder-decoder

## Definition of the task

LSTM encoder-decoder architecture for number sorting.

## Solution

1. Data Preparation:

   Write a method to generate random integers in certain range and sort these integers. In this case the range is between 1 to 1000. 

   Example [355, 121, 926, 961, 88, 773, 673, 218] [88, 121, 218, 355, 673, 773, 926, 961]

2. Then convert lists to Numpy Arrays and rescale the values to fit within the bounds of the activation used by LSTM.

3. Create LSTM model:

   Createa Keras model with Sequential() constructor and add LSTM layer. The ADAM optimization is used to fit the model.

4. Train model:

   Fit the model on data for 5 epochs. Evaluate the model for new patterns. 

### Folder structure

```shellcript
dir LSTM_encoder_decoder
encoder_decoder.ipynb
encoder_decoder.py
```

where
- encoder_decoder.py/ is the main python script to implement the requirements of the task.
- encoder_decoder.ipynb is the python script from google colab which runs the code as a block. It contains block of codes along with output.

### How to run the script

> Once the encoder_decoder.ipynb is opened, please click on "open


