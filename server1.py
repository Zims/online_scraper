from flask import Flask, render_template, request, Blueprint, jsonify
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

@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files[0]


@app.route('/output')
def otput_folder():
   return render_template('files.html')

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
