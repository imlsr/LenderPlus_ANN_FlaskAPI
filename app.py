from flask import Flask,request,jsonify
import numpy as np
from tensorflow.keras.models import load_model

def predict_v2(l):
    x = (l[1]*l[3])/(l[2]*l[0])
    return (1-(1/(1+x)))*100

def return_prediction(model,sample_json):

  l_amnt = sample_json["loan_amnt"]
  t = sample_json["term"]
  i_rate = sample_json["int_rate"]
  a_inc = sample_json["annual_inc"]

  loan = [l_amnt,t,i_rate,a_inc]

  #loan_status_pred = model.predict(loan)[0]
  loan_status_pred = predict_v2(loan)

  return loan_status_pred



app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>RUNNING</h1>'

p2p_model = load_model('lending.h5',compile=False)


@app.route('/params')
def params():

    loan_amnt = int(request.args['loan_amnt'])
    term = int(request.args['term'])
    int_rate = float(request.args['int_rate'])
    annual_inc = int(request.args['annual_inc'])

    loan = [loan_amnt,term,int_rate,annual_inc]

    print(loan)

    return str(predict_v2(loan))

@app.route('/api/p2p',methods=['POST'])

def loan_prediction():
    content = request.json

    results = return_prediction(p2p_model,content)

    return jsonify(str(results))

if __name__=='__main__':
    app.run()