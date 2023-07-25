'''
Purpose : Generating C files (source and header) of the quantized model that will be included in the IDE Project 
Author  : Ayat B.
'''
#-------------------------------------------------------- Imports -------------------------------------------------------- 
import post_train_quantization
from tensorflow.lite.python.util import convert_bytes_to_c_source

# -------------------------------------------------------- Generating C files -----------------------------------------------
tflite_model = post_train_quantization.tflite_quantized_model
from tensorflow.lite.python.util import convert_bytes_to_c_source

source_text, header_text = convert_bytes_to_c_source(tflite_model, "CNN2D_model")

with  open('../Models/CNN2D_quantized_model.h',  'w')  as  file:
    file.write(header_text)

with  open('../Models/CNN2D_quantized_model.cc',  'w')  as  file:
    file.write(source_text)