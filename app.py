from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'data-analysis',
    'location': 'pune',
    'salary': '$4000'
}, {
    'id': 2,
    'title': 'data-scientist',
    'location': 'bangluru',
    'salary': '$5000'
}, {
    'id': 3,
    'title': 'front-end-engineer',
    'location': 'hydrabad',
    'salary': '$6000'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

@app.route("/")
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
