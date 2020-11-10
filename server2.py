from flask import Flask, render_template, request, Blueprint
import soup_yp

app = Flask(__name__)

# f = open("roofer.json", "r")
# data = f.read()
admin = Blueprint('admin', __name__, static_folder='static')


@app.route("/", methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    input_url = request.form['Name']
    file_name = request.form['Filename']
    return f'Input URL is <br>{input_url}<br><br> And filename is<br>{file_name}'
