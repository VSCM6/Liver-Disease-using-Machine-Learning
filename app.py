import numpy as np
import pickle
from flask import Flask, request, jsonify, render_template


# Create flask app
flask_app = Flask(__name__,template_folder="template")
model=pickle.load(open("LiverDisease.p","rb"))
@flask_app.route("/")
def Home():
    return render_template("index.html")

gender={'Male':1 ,'Female':0}
Disease={1:"Liver Disease",2:"Mon Liver Disease"}
@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features =[]
    float_features.append(int(request.form['age']))
    float_features.append(gender[request.form['gender']])
    float_features.append(request.form['Total_Bilirubin'])
    float_features.append(request.form['Direct_Bilirubin'])
    float_features.append(request.form['Alkphos_Alkaline_Phosphotase'])
    float_features.append(request.form['SgptAl_amine_Aminotransferase'])
    float_features.append(request.form['Sgot_partate_Aminotransferase'])
    float_features.append(request.form['Total_Protiens'])
    float_features.append(request.form['ALB_Albumin'])
    float_features.append(request.form['A/G_Ratio_Albumin_and_Globulin_Ratio'])
    float_features=np.array(float_features)
    float_features=float_features.reshape(1,-1)
    predict=model.predict(float_features)
    result=Disease[predict[0]]
    return render_template("index.html", prediction_text = "You have {}".format(result))

if __name__ == "__main__":
    flask_app.run(debug=True)