from flask_pymongo import PyMongo
import flask
import pymongo
import dns
from flask import request

app = flask.Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://Sarthak:Sarthak@mycluster.rk40e7p.mongodb.net/MyDB?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)

@app.route("/save_file", methods=['POST', 'GET'])
def POST():
    if request.method == 'POST':
       uploaded_file = request.files['file']
       if uploaded_file.filename != '':
          mongodb_client.save_file(uploaded_file.filename, uploaded_file)
          return {"file name": uploaded_file.filename}
       else:
          return "Error"

if __name__ == "__main__":
    app.run(debug=True)
