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
       model = models.replace(")","").split("(")
       if model[0] == 'symptom':
         print(model[1])

       if model[0] == 'diagnosis':
         print(model[1])

       if model[0] == 'treatment':
         print(model[1])
         treatments = model[1].split(",")
         for treatment in treatments:
            print(treatment.strip())


    return render_template("diagnosis.html",result = symptoms)

if __name__ == '__main__':
   app.run(debug = True)