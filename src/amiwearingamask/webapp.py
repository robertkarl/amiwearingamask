import flask

import fastai
from fastai.vision import load_learner


bp = flask.Blueprint("webapp", __name__)
model = load_learner('model')

classes = ['mask', 'nomask']
def get_prediction_name(image_name):
    image = fastai.vision.open_image(image_name)
    val = model.predict(image)
    argmaxres = val[1].argmax()
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
        img_name = 'tmp.png'
        if 'input_image' in flask.request.files:
            flask.request.files['input_image'].save('tmp.png')
        else:
            import base64
            b64 = flask.request.values['image'].split(',')[1]
            with open('tmp.png', 'bw') as f:
                f.write(base64.decodebytes(bytes(b64, 'UTF-8')))
        val = get_prediction_name(img_name)
        return flask.jsonify({'prediction': val})
    return flask.render_template('masked.html', result=val)

