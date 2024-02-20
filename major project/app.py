from flask import Flask, render_template,request
import numpy as np
import pickle
app = Flask(__name__)
model = pickle.load(open(r"C:\Users\Akhila Potla\OneDrive\Desktop\major project\Genetic-classification.pkl",'rb'))
@app.route('/')
def Home():
    return render_template('index.html')
@app.route('/About')
def About():
    return render_template('About.html')
@app.route('/Prediction')
def Prediction():
    return render_template('Prediction.html')
@app.route('/Prediction',methods=["POST","GET"])
def prediction():
    
    x = [int(x) for x in request.form.values()]
    x=np.array(x)
    
    prediction=model.predict([x])
    
    if (prediction==0):
        return render_template("Prediction.html",predict="Clinical variant Classification")
    else:
        return render_template("Prediction.html",predict=" conflicting variant classification")
    
if __name__=="__main__":
    app.run(debug = True,port = 1234)
if __name__=="__main__":
    app.run(debug = True,port = 1212)