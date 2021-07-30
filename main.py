from flask import Flask, render_template, request
import collections
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

    diagnosis = []
    treatments = collections.defaultdict(list)

    for models in aspmodel:
       model = models.replace(")","").split("(")

       if model[0] == 'diagnosis':
         diagnosis.append(model[1].capitalize())

       if model[0] == 'treatment':
         treatment = model[1].split(",")
         treatments[treatment[0]].append(treatment[1].strip())
         treatments[treatment[0]].append('test')
       print(treatments)


    return render_template("diagnosis.html",result = symptoms, diagnosis = diagnosis, treatments = treatments)

if __name__ == '__main__':
   app.run(debug = True)