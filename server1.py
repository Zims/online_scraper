from flask import Flask, render_template, request
import soup_yp

app = Flask(__name__)

# f = open("roofer.json", "r")
# data = f.read()
# f = open("top_30.json", "r")
# top_30_data = f.read()


@app.route("/", methods=['GET'])
def index():
    return render_template('/index.html')

@app.route('/input')
def input():
   return render_template('input.html')

@app.route('/output')
def student():
   return '/output'

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form

    # how to parse the flask dict:
    # https://stackoverflow.com/questions/23205577/python-flask-immutablemultidict
      the_url = request.form.getlist('Name')
      file_name_chosen = request.form.getlist('Filename')

      print(the_url)
      print(file_name_chosen)
      soup_yp.output_file(the_url[0], file_name_chosen[0])

      return render_template("result.html",result = result)

#   gunicorn server1:app

# ngrok->
#   ngrok http 8000
