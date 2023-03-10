import numpy as np
import os
from scipy import  misc
from keras.models import model_from_json
import pickle,cv2

# Loading int2word dict
classifier_f = open("int_to_word_out.pickle", "rb")
int_to_word_out = pickle.load(classifier_f)
classifier_f.close()

def load_model():
    # load json and create model
    json_file = open('model_face.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_face.h5")
    print("Loaded model from disk")
    return loaded_model

def pre_process(image):
    image = image.astype('float32')
    image = image / 255.0
    return image

def load_image():
    # img=os.listdir("images")[0]
    image=np.array(cv2.imread(r"C:\projects\image-classification\Brain_Data_Organised\Stroke\68 (1).jpg"))
    # cv2.imshow('image',image)
    # cv2.waitKey(0)
    image = cv2.resize(image, (64, 64))
    image=np.array([image])
    image=pre_process(image)
    return image

image=load_image()
model=load_model()

prediction=model.predict(image)

print(prediction)
print(np.max(prediction))
print(int_to_word_out[np.argmax(prediction)])
