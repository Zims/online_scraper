from flask import Flask, render_template, request, Blueprint, jsonify, send_from_directory
from flask.helpers import send_file
import soup_yp
import os

app = Flask(__name__)

UPLOAD_DIRECTORY = "/"

# f = open("roofer.json", "r")
# data = f.read()
admin = Blueprint('admin', __name__, static_folder='static')


@app.route("/", methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/input')
def input():
   return render_template('input.html')


@app.route('/output')
def otput_folder():
   return send_from_directory('./output', 'co.json')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

    # how to parse the flask dict:
    # https://stackoverflow.com/questions/23205577/python-flask-immutablemultidict
      the_url = request.form.getlist('Name')
      file_name_chosen = request.form.getlist('Filename')

      soup_yp.output_file(the_url[0], file_name_chosen[0])

      return render_template("result.html",result = result)

#   gunicorn server1:app

# ngrok->
#   ngrok http 8000
