import flask
import random
import os

import fastai
from fastai.vision import load_learner
import logging

bp = flask.Blueprint("webapp", __name__)
learner = None
classes = ['mask', 'nomask']

def get_prediction_name(image_name):
    image = fastai.vision.open_image(image_name)
    global learner
    if not learner:
        logging.error('Initializing the model.')
        learner = load_learner('model')
    val = learner.predict(image)
    argmaxres = val[2].argmax()
    highest_category = argmaxres.item()
    res = classes[highest_category]
    return res

@bp.route('/webcam', methods=["GET", "POST"])
def webcam():
    return flask.render_template('webcam.html')


@bp.route('/', methods=["GET", "POST"])
def predict():
    val = None
    if flask.request.method == 'POST':
        img_name = 'tmp-{}.png'.format(random.randint(1000,9999))
        if 'input_image' in flask.request.files:
            flask.request.files['input_image'].save(img_name)
        else:
            import base64
            b64 = flask.request.values['image'].split(',')[1]
            with open(img_name, 'bw') as f:
                f.write(base64.decodebytes(bytes(b64, 'UTF-8')))
        val = get_prediction_name(img_name)
        os.unlink(img_name)
        return flask.jsonify({'prediction': val})
    return flask.render_template('masked.html', result=val)

