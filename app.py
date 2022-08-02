from flask import Flask
from datetime import datetime

from flask import render_template, request

app = Flask(__name__)
def myConvert(amount):
    return amount * 1.18
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
@app.route('/result', methods=['GET', 'POST'])
def result():
    myformData = request.form.get('pounds')
    myformData = int(myformData)
    myConversion = myConvert(myformData)

    myDTnow = datetime.now()




    return render_template('result.html', myformData=myformData, myConversion=myConversion)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)