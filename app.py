from flask import Flask
from datetime import datetime
from flask import render_template, request


shopOpenTime = '09:00:00'
shopCloseTime = '17:00:00'
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#function to render result
@app.route('/result', methods=['GET', 'POST'])
def result():
  thisShopOpenClosed = isTheShopCurrentlyOpen(shopOpenTime, shopCloseTime, currentTime)
  return render_template('result.html', resultOpenClosedState=thisShopOpenClosed, resultDTnow=currentTime)


#Function to check if the shop is open
def isTheShopCurrentlyOpen(thisShopOpenTime, thisShopCloseTime, thisCurrentTime):
  if (thisCurrentTime > thisShopOpenTime) and (thisCurrentTime < thisShopCloseTime):
    return 'open'
  else:
    return 'closed'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

