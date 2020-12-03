# LSTM encoder-decoder

## Definition of the task

LSTM encoder-decoder architecture for number sorting.

## Solution

1. Data Preparation

Write a method to generate random integers in certain range and sort these integers. In this case the range is between 1 to 1000. 

Example [355, 121, 926, 961, 88, 773, 673, 218] [88, 121, 218, 355, 673, 773, 926, 961]

2. Then convert lists to Numpy Arrays and rescale the values to fit within the bounds of the activation used by LSTM.

3. Create LSTM model

Createa Keras model with Sequential() constructor and add LSTM layer. The ADAM optimization is used to fit the model

4. Train model

Fit the model on data for 5 epochs. Evaluate the model for new patterns. 

### Folder structure

```shellcript
dir LSTM_encoder_decoder
encoder_fibonaaci.py
```

where
- docs/ is the folder setup to generate documentation of the source code using python package sphinx
- fibonacci/ is the placeholder which implements the requirements of the task as submodule and it also includes the tests
- flask_fibonaaci.py is the main python script which will be used to created the end points using flask framework.

### How to run the script

> Please use two terminals simultaneously

1. In terminal 1

```console
cd python_flask_fibonacci
python flask_fibonaaci.py
```

1.1 Expected results

```console
 * Serving Flask app "flask_fibonaaci" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 132-959-924
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```

2. In terminal 2

```console
cd python_flask_fibonacci
curl http://127.0.0.1:5000/fib/your_number
```

2.1

> Here the integer 11 has been taken as an example.

```console
curl http://127.0.0.1:5000/fib/11
{
  "result": [
    [
      3,
      8
    ],
    [
      3,
      3,
      5
    ],
    [
      2,
      2,
      2,
      5
    ],
    [
      2,
      3,
      3,
      3
    ],
    [
      2,
      2,
      2,
      2,
      3
    ]
  ]
}
```

## About documents

> install supporting packages and perform steps as shown below in order to generate the documentation out of source code.

```console
pip install sphinx
pip install sphinx_rtd_theme
pip install sphinx-argparse
cd python_flask_fibonacci
sphinx-build -b html docs build-docs
```


1. Go to build-docs\index.html
