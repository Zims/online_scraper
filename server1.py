from flask import Flask, render_template, request
import soup_yp

app = Flask(__name__)

f = open("roofer.json", "r")
data = f.read()

f = open("top_30.json", "r")
top_30_data = f.read()

@app.route("/", methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/input')
def student():
   return render_template('input.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

@app.route('/result')
def result():
    return soup_yp.output_file()

@app.route("/files.html", methods=['GET'])
def files():
    return render_template('/files.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['GET', 'POST'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

@app.route("/top_30.html", methods=['GET'])
def top_30():
    return top_30_data

    
# @app.route("/tester", methods=['GET'])
# def tester():
#     return data

# Start the server in terminal:

#   python3 -m http.server
# w/o pipenv but in the right directory. With index file in it

#   gunicorn server1:app

# ngrok->
#   ngrok http 8000
