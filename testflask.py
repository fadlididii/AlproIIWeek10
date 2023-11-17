import csv
import json
from io import StringIO
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

def csv2json(data):
	reader = csv.DictReader
	reader = csv.DictReader(data)
	out = json.dumps([ row for row in reader ])
	print ("JSON parsed!")
	return out
	print ("JSON saved!")

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

@app.route("/")
def hello_world():
    return '<p>Hello World</p>'

@app.route('/biodata/')
def  biodata():
    return render_template('biodata.html')

@app.route('/cv/')
def  cv():
    return render_template('cv.html')

@app.route('/portofolio/')
def  portofolio():
    return render_template('portofolio.html')

@app.route('/f1/')
def  f1():
    return render_template('f1.html')

@app.route('/cat/')
def  cat():
    return render_template('cat.html')

@app.route('/fibonacci/', methods=['GET', 'POST'])
def fib():
    if request.method == 'POST':
        num = int(request.form['number'])
        series = fibonacci(num)
        return render_template('fibonacci.html', series=series, num=num)
    return render_template('fibonacci.html')

@app.route('/csvtojson', methods=["POST"])
def convert():
	f = request.files['data_file']
	if not f:
		return "No file"
	file_contents = StringIO(f.stream.read().decode('utf-8'))
	result = csv2json(file_contents)
	response = make_response(result)
	response.headers["Content-Disposition"] = "attachment; filename=Converted.json"
	return response

@app.route('/convert')
def main():
	render_template
	return render_template('convert.html')

@app.route('/form/', methods=['GET', 'POST'])
def submit_form():
    form_data = None
    if request.method == 'POST':
        form_data = request.form
    return render_template('form.html', form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
