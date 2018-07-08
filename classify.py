import os.path,sys
os.environ['KERAS_BACKEND'] = 'theano'
from keras.models import Model
from keras.models import load_model
from PIL import Image
import numpy as np
import pandas as pd

IMAGE_SIZE = 224

model = load_model('amimage.hdf5')
model.summary()
categories = ["melon","suica","takenoko","yacon"]
fnames = [name for name in os.listdir("./predict") if name != ".DS_Store"]

print("---start predictions---")
print(categories)
X = []
for fname in fnames:
    img = Image.open("./predict/" + fname)
    img = img.convert("RGB")
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    in_data = np.asarray(img) / 255
    X.append(in_data)
X = np.array(X)

predictions = model.predict(X)
i = 0
for p in predictions:
    print(fnames[i] + " must be " + categories[p.argmax()])
    i = i + 1
