import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import load_model

#Initializing the CNN
classifier = Sequential()
classifier = load_model('gestures')

import numpy as np

def predict(filename):
    from keras.preprocessing import image
    test_image = image.load_img(filename, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    print (result)
    if result[0][0] == 1:
        prediction = '0'
    elif result[0][1] == 1:
        prediction = '1'
    elif result[0][2] == 1:
        prediction = '2'
    elif result[0][3] == 1:
        prediction = '3'
    elif result[0][4] == 1:
        prediction = '4'
    elif result[0][5] == 1:
        prediction = '5'
    elif result[0][6] == 1:
        prediction = '6'
    elif result[0][7] == 1:
        prediction = '7'
    elif result[0][8] == 1:
        prediction = '8'
    elif result[0][9] == 1:
        prediction = '9'
    return prediction
# print(prediction)