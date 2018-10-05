#!/usr/bin/env python

import tensorflow as tf
from tensorflow import keras


# (x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()

'''
{"class_name": "Sequential", "config": [{"class_name": "Dense", "config": {"name": "dense_1", "trainable": true, "batch_input_sha
pe": [null, 1], "dtype": "float32", "units": 16, "activation": "relu", "use_bias": true, "kernel_initializer": {"class_name": "Va
rianceScaling", "config": {"scale": 1.0, "mode": "fan_avg", "distribution": "uniform", "seed": null}}, "bias_initializer": {"clas
s_name": "Zeros", "config": {}}, "kernel_regularizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_cons
traint": null, "bias_constraint": null}}, {"class_name": "Dense", "config": {"name": "dense_2", "trainable": true, "units": 12700
, "activation": "linear", "use_bias": true, "kernel_initializer": {"class_name": "VarianceScaling", "config": {"scale": 1.0, "mod
e": "fan_avg", "distribution": "uniform", "seed": null}}, "bias_initializer": {"class_name": "Zeros", "config": {}}, "kernel_regu
larizer": null, "bias_regularizer": null, "activity_regularizer": null, "kernel_constraint": null, "bias_constraint": null}}, {"c
lass_name": "Activation", "config": {"name": "activation_1", "trainable": true, "activation": "sigmoid"}}, {"class_name": "Reshap
e", "config": {"name": "reshape_1", "trainable": true, "target_shape": [50, 254]}}]}

{"optimizer_config": {"class_name": "Adam", "config": {"lr": 0.0010000000474974513, "beta_1": 0.8999999761581421, "beta_2": 0.9990000128746033, "decay": 0.0, "epsilon": 1e-07, "amsgrad": false}}, "loss": "binary_crossentropy", "metrics": ["accuracy", "mae"], "sample_weight_mode": null, "loss_weights": null}
'''

loaded_model = keras.models.load_model('learn_my_flag.hdf5')

help(loaded_model)
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
loaded_model.evaluate( steps = 10 )

# loaded_model.fit(x_train, y_train, epochs=5, batch_size=32)

# import h5py
# filename = 'learn_my_flag.hdf5'
# f = h5py.File(filename, 'r')

# # List all groups
# print("Keys: %s" % f.keys())
# model_weights = f['model_weights']
# optimizer_weights = f['optimizer_weights']

# print optimizer_weights