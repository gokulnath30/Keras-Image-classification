import pickle
import numpy as np
import os
import cv2

# Loading dataset
def load_datasets():
    X=[]
    y=[]
    for image_label in label:
        images = os.listdir("Brain_Data_Organised/"+image_label)
        for image in images:
            img = cv2.imread("Brain_Data_Organised/"+image_label+"/"+image)
            img = cv2.resize(img, (64, 64))
            X.append(img)
            y.append(label.index(image_label))
 
    X=np.array(X)
    y=np.array(y)
    return X,y

# Save int2word dict
label = os.listdir("Brain_Data_Organised")
save_label = open("int_to_word_out.pickle","wb")
pickle.dump(label, save_label)
save_label.close()
