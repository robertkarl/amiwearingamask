import flask
import fastai

bp = flask.Blueprint("webapp", __name__)

@bp.route('/asdf')
def asdf():
    return flask.render_template('asdf.html')
