# from flask import Flask
# from ..config import DevConfig

# # Initialize the app
# app = Flask(__name__, instance_relative_config=True)

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


# from .main import views


from flask import Flask
from config import config_options

def create_app(config_name):

    app = Flask(__name__)

    #Creating the app from configurations
    app.config.from_object(config_options[config_name])

    return app