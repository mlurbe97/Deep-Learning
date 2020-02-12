# Deep Learning

## Authors

* Manel Lurbe Sempere (malursem@inf.upv.es)

## Documentation

- Folder *doc* contains a book of keras introduction and demos.
- Another interesting book in torres.ai (2 parts) [Read online](https://torres.ai/deep-learning-inteligencia-artificial-keras)

# Tensorflow

You must install tensorflow in order to execute the code in the folder *Tensorflow*, or you can use an online platform as google colabs to test without installing anything [Go to Google Colabs](https://colab.research.google.com)

# Python install and libs

For Ubuntu:

- Install python for develop:

```sudo apt install python-dev python-pip python3-dev python3-pip python-tk python3-tk python3-sklearn python3-sklearn-lib python3-sklearn-doc```

- Install libs for python 2:

```sudo pip install numpy pandas matplotlib tensorflow bigml matplotlib```

**Note: This will install Tensorflow CPU version.**

- Install libs for python 3 (recomended):

```sudo python3 -m pip install numpy pandas matplotlib tensorflow bigml matplotlib```

**Note: This will install Tensorflow CPU version.**

- Install Jupyter Notebook:

```sudo python3 -m pip install notebook```

- Install pip-review to check the lastest version of the libs:

```sudo python3 -m pip install pip-review```

- Upgrade libs to latest stable versions:

```sudo pip-review --local --interactive```

- Optional install *Visual Studio Code* which is compatible with jupyter notebook server [Get Visual Studio Code](https://code.visualstudio.com/download)

# Install CUDA for Tensorflow

Installing CUDA for computers with Nvidia graphics card will reduce processing time.
You must install Nvidia compatible driver with the version of CUDA used and install Tensorflow for GPU. [Official doc](https://www.tensorflow.org/install/gpu)

