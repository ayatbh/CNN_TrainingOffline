'''
Author  : Ayat B.
Purpose : Optimize the TFlite by applying a post-training quantization
'''
# Includes
import tensorflow as tf
from tensorflow import lite
import numpy as np
import pandas as pd


# Load your trained float32 model
model = tf.keras.models.load_model('../Models/modelCNN2D.h5')

# Define a representative dataset generator function
def representative_dataset_generator():
    for input_data in training_data:
        yield [input_data[np.newaxis,:].astype(np.float32)] 

#------------------------------------------------------ Representative dataset ----------------------------------------------------------------
# Load the training dataset from the .npy file
training_data = np.load('..\\numpy_dataset\\X_test.npy')

#--------------------------------------------------------- Quantization -----------------------------------------------------------------
# Convert the model to a TensorFlow Lite model with int8 quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.representative_dataset = representative_dataset_generator
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]

# Configure the input and output types for inference to be int8 
converter.inference_input_type = tf.float32
converter.inference_output_type = tf.float32

# Convert the model to the quantized TensorFlow Lite model 
tflite_quantized_model = converter.convert()

# Save the quantized model to a file
with open('../Models/quantized_model.tflite', 'wb') as f:
    f.write(tflite_quantized_model)
