from flask import Flask, render_template, request
from os import system

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('symptoms.html')

@app.route('/diagnosis',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
    symptoms = request.form.getlist('symptoms')

    f = open("symptoms.sm", "w")
    for symptom in symptoms:
      f.write('symptom('+symptom.lower()+').\n')
    f.close()

    system(".\dependencies\clingo.exe .\symptoms.sm .\diagandtreat.sm | .\dependencies\mkatoms.exe > results.sm")

    results = open('results.sm','r')
    aspmodel = results.readlines()

    for models in aspmodel:
       print(models)
    return render_template("diagnosis.html",result = symptoms)

if __name__ == '__main__':
   app.run(debug = True)