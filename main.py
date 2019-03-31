from flask import Flask, render_template, request
import json
import addRecord
import deleteScript
import getRecord
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('gui.html')
    
    name = request.form['fullname']
    email = request.form['email']
    number = request.form['phone']
    drug = request.form['prescription']
    dose = request.form['dosage']
    
    id = addRecord.newUser(name, email, number, drug, dose)
    print("ID: ",id.json())

    return render_template('gui.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    return render_template('main.html')

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        data_json = {}
        return render_template('check.html', data_list=data_json)
    
    id = request.form['ID']
    data_json = getRecord.getRecord(id)

    return render_template('check.html', data_list=data_json)

@app.route('/issue', methods=['GET', 'POST'])
def issue():
    if request.method == 'GET':
        return render_template('Output.html')
    
    id = request.form['ID']
    deleteScript.deleteRecord(id)

    return render_template('Output.html')

@app.route('/getall',  methods=['GET', 'POST'])
def getall():
    payload = {'X-Username': 'kushal.jhunjhunwalla@gmail.com', 'X-Api-Key' : 'QKGs+DurASnHUPuR21MyiONYYR3XAtOKtOf04xYzUIA=',
            'Content-Type': 'application/json'}
    url = " https://api.tierion.com/v1/records?datastoreId=7132"
    response = requests.get(url, headers = payload)
    print("RES: ",response.json())
    return None

if __name__ == '__main__':
    app.run(debug=True)
