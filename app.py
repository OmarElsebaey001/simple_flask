from flask import make_response,Flask,render_template
from flask import request, jsonify

app = Flask(__name__)
@app.route("/",methods=['GET'])
def show():
    return "Hellooooooooo"
       
