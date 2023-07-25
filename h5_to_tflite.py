'''
Author  : Ayat B.
Purpose : Converting the h5 file to TFLite file
'''

import tensorflow as tf
from tensorflow import keras
model = tf.keras.models.load_model('../Models/modelCNN2D.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
#converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

open("../Models/CNN2D_model.tflite", "wb").write(tflite_model)



