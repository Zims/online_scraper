from flask import Flask, render_template
import soup_yp

app = Flask(__name__)

f = open("roofer.json", "r")
data = f.read()

f = open("top_30.json", "r")
top_30_data = f.read()

# @app.route("/", methods=['GET'])
# def prime():
#     return "/index.html"

@app.route("/", methods=['GET'])
def index():
    return render_template('/index.html')

@app.route("/input_url.html", methods=['GET'])
def input_url():
    return render_template('/input_url.html')


@app.route("/files.html", methods=['GET'])
def files():
    return render_template('/files.html')


@app.route("/f1.html", methods=['GET'])
def f1():
    return data

# @app.route('"/top_30.html"')
# def dynamic_page():
#     return soup_yp.output_file()


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
