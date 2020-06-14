import flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = flask.Flask(__name__, instance_relative_config=True)
    from amiwearingamask import webapp
    app.register_blueprint(webapp.bp)
    return app
