# app.py
from flask import Flask
import os

app = Flask(__name__)

# Feature flag
NEW_FEATURE = os.getenv("NEW_FEATURE") == "true"
TEAM_NAME = os.getenv("TEAM_NAME")


@app.route('/')
def hello_world():
    if NEW_FEATURE:
        return 'New Feature is ON!'
    else:
        return 'Old Feature is running.'

@app.route('/test')
def team_name():
    if NEW_FEATURE:
        return "{0} are not idle.".format(TEAM_NAME)
    else:
        return "we don't know what we're doing."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')