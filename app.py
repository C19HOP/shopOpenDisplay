from flask import Flask
from datetime import datetime
from flask import render_template, request


shopOpen = '09:00:00'
shopClose = '17:00:00'
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
myOpenClosedState = ''

app = Flask(__name__)
def myConvert(amount):
    return amount * 1.18

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
  
  if (current_time > shopOpen) and (current_time < shopClose):
    myOpenClosedState = 'open'
  else:
    myOpenClosedState = 'closed'

  return render_template('result.html', resultOpenClosedState=myOpenClosedState, resultDTnow=current_time)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)