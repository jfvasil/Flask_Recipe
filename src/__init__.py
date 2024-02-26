from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

from flask import Flask
from flask_bootstrap import Bootstrap
from src import routes
from src.config import Config


app = Flask(__name__)

Bootstrap(app)


app.config.from_object(Config)



app.register_blueprint(routes.bp)

if __name__ == '__main__':
    app.run


