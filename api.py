import os.path,sys
from bottle import route, run
os.environ['KERAS_BACKEND'] = 'theano'
from keras.models import Model
from keras.models import load_model
from PIL import Image
import numpy as np
IMAGE_SIZE = 224
model = load_model('amimage.hdf5')
categories = ["メロン","スイカ","たけのこ","ヤーコン"]

@route('/amimage/predict/')
def predict():
    X = []
    img = Image.open("./predict/" + "suica.jpg")
    img = img.convert("RGB")
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    in_data = np.asarray(img) / 255
    X.append(in_data)
    X = np.array(X)
    predictions = model.predict(X)
    for p in predictions:
        return categories[p.argmax()]


run(host='localhost', port=8080, debug=True)
