
'''
Purpose . Generating C files (source and header) that will be included in the IDE Project 
Author  : Ayat B.
'''
#-------------------------------------------------------- Imports -------------------------------------------------------- 
import h5_to_tflite
from tensorflow.lite.python.util import convert_bytes_to_c_source

# -------------------------------------------------------- Generating C files ---------------------------------------------------------------------- 
tflite_model = h5_to_tflite.tflite_model
from tensorflow.lite.python.util import convert_bytes_to_c_source

source_text, header_text = convert_bytes_to_c_source(tflite_model,  "CNN2D_model")

with  open('../Models/CNN2D_model.h',  'w')  as  file:
    file.write(header_text)

with  open('../Models/CNN2D_model.cc',  'w')  as  file:
    file.write(source_text)