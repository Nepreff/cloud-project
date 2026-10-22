import os
from flask import Flask

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Cloud project")


@app.route('/')
def index():
    return f'{APP_NAME} is running in Docker!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
