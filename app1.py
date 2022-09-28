from flask import Flask, return_template

app1 = Flask(__name__)


@app1.route("/")
def Hello_World():
    return_template(app1.py)
