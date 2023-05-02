import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


PORT = os.environ["PORT"]

@app.route("/index")
def index():
    return "hello world"
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= False, port= PORT)
