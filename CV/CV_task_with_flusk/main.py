import os
import pandas as pd

from keras.preprocessing.image import load_img, img_to_array
from tensorflow import keras as kr
from flask import Flask, render_template, request

un = pd.read_csv('unique.csv')
labels = un.Label.to_list()


# Process image and predict label
def predict_image(image):
    model = kr.models.load_model('model.h5')
    test_image = load_img(image, target_size=(224, 224))
    test_image = img_to_array(test_image)

    test_image = test_image.reshape((1, test_image.shape[0], test_image.shape[1], test_image.shape[2]))
    test_image = kr.applications.resnet_v2.preprocess_input(test_image)
    result = model.predict(test_image)[0].argmax()

    return labels[result]


# Initializing flask application
image_folder = os.path.join('static', 'images')
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = image_folder


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imagefile = request.files['imagefile']
    image_path = 'static/images/' + imagefile.filename
    imagefile.save(image_path)
    pic = os.path.join(app.config['UPLOAD_FOLDER'], imagefile.filename)
    prediction = predict_image(pic)
    return render_template('index.html', user_image=pic, prediction_text='The test image is {}'.format(prediction))


if __name__ == '__main__':
    app.run()