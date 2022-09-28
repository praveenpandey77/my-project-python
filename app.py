from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World, great india"


print("hello india")
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

print("india is great")
#updated comment