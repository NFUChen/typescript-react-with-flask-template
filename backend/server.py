from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/index")
def index():
    return "hello world"
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= False, port= 8080)
