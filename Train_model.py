'''
Purpose : Create a 2D CNN model and train it 
           (=✪㉨✪=)
'''
#-------------------------------------------------------- Imports -------------------------------------------------------- 
import tensorflow as tf
import pandas as pd
import numpy as np


print(tf. __version__)
CUDA_VISIBLE_DEVICES=0
#-------------------------------------------------------- Functions -------------------------------------------------------- 
# Creating a CMNN 2D model 
def create_model(timesteps, features, outputs) :
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape=(timesteps,features,1)))
    model.add( tf.keras.layers.Conv2D(filters=8, kernel_size=(4,2), activation='relu', padding='same'))
    model.add( tf.keras.layers.Dropout(0.5))
    model.add( tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add( tf.keras.layers.Conv2D(filters=4, kernel_size=(3,2), activation='relu', padding='same'))
    model.add( tf.keras.layers.Dropout(0.5))
    model.add( tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
    model.add( tf.keras.layers.Conv2D(filters=1, kernel_size=(1, 1), activation='linear', padding='same'))
    model.add( tf.keras.layers.Flatten())  
    model.add( tf.keras.layers.Dense(outputs, activation='softmax')) 
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # fit network
    model.summary()
    return model 

# Printing the training accuracy 
class PrintTrainingAccuracy(tf.keras.callbacks.Callback):
    def __init__(self, total_epochs):
        super(PrintTrainingAccuracy, self).__init__()
        self.total_epochs = total_epochs
    
    def on_epoch_end(self, epoch, logs=None):
        if epoch == self.total_epochs - 1:
            train_acc = logs['accuracy']
            print(f'Training Accuracy: {train_acc:.4f}')

#------------------------------------------------------------- Loading the dataset ----------------------------------------------------------------------------
path2load = '../numpy_dataset/'
X_train = np.load(path2load + 'X_train.npy')
y_train = np.load(path2load + 'y_train.npy')
X_val = np.load(path2load + 'X_val.npy')
y_val = np.load(path2load + 'y_val.npy')
X_test = np.load(path2load + 'X_test.npy')
y_test = np.load(path2load + 'y_test.npy')

n_classes = len(y_train[0])

# -------------------------------------------------------- Training & Evaluating the model ---------------------------------------------------------------------- 
timesteps = 80
features = 16
outputs = n_classes
total_epochs = 50
print_acc_callback = PrintTrainingAccuracy(total_epochs)


model = create_model(timesteps, features, outputs)
model.fit(X_train, y_train, epochs=total_epochs, callbacks=[print_acc_callback], verbose=0) # Training 
_, val_acc = model.evaluate(X_val, y_val, verbose=0) # Evaluation 
print("Validation accuracy : {} ".format(val_acc))

#------------------------------------------------------------------------ Saving the best model ---------------------------------------------------
model.save('../Models/modelCNN2D.h5')

#Test Model 
_, test_acc = model.evaluate(X_test, y_test, verbose=0) # Evaluation 
print("Test accuracy : {} ".format(test_acc))
