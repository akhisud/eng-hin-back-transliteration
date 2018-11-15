
# eng-hin-back-transliteration

## Requirements

* Python 2.7
* Keras 2.0.8+ with Tensorflow backend

## Description

This repository contains code, models and data for the task of English-to-Hindi transliteration

## Code

* Datasets contains the dataset for transliteration. This was obtained from the Fire 2013 track on transliterated search, more specifically from here.
    * [Bollywood_dataset.txt](Bollywood_dataset.txt) contains the above data
    * [Noisy_bollywood.txt](Noisy_bollywood.txt) is an artificial-noise injected dataset by random mutation, removal or addition of characters to the English words
    * [Bollywood_oversampled.txt](Bollywood_oversampled.txt) contains oversampled data, where the different English transliterations of each Hindi word are sampled equally.
* eng_hin_simple has code for training and testing
    * [data.py](data.py) has helper functions for loading data
    * [prog.py](prog.py) has the training and testing code, that trains on Bollywood_dataset.txt by default, and can be modified to train on any other datasets.
    * [model.png](model.png) has the diagram of the model
    * The best model is saved to saved_model.hdf5
* [try.py](try.py) is the inferencing script, to transliterate a set of english words from a file (path to be set inside script) 
* [typing_noise.py](typing_noise.py) is an experimental script to model noise in spellings of words, based on QWERTY keyboards' proximity of character pairs 

