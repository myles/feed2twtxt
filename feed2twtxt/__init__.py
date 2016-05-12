import os

from flask import Flask

from flask_appconfig import HerokuConfig

from .frontend import frontend


def create_app(configfile=None):
    app = Flask(__name__)

    HerokuConfig(app, configfile)

    app.register_blueprint(frontend)

    return app


app = create_app()

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port, debug=True)
