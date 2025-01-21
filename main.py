from flask import Flask, render_template, request
import requests


app = Flask(__name__)
# Create a dictionary to store the credentials
credentials = {'apiUrl': 'https://7105.api.greenapi.com'}


@app.route('/', methods=['GET', 'POST'])
def index():
    # Add the credentials to the dictionary
    if request.form:
        for key in request.form.keys():
            credentials[key] = request.form[key]
    # Create variables to store information
    payload, headers = {}, {}

    if request.method == 'POST':
        if request.form['action'] == 'getSettings':
            # Create the URL to create the request
            url = f"{credentials['apiUrl']}/waInstance{credentials['idInstance']}/getSettings/{credentials['apiTokenInstance']}"
            response = requests.request("GET", url, headers=headers, data=payload)

        elif request.form['action'] == 'getStateInstance':
            # Create the URL to create the request
            url = f"{credentials['apiUrl']}/waInstance{credentials['idInstance']}/getStateInstance/{credentials['apiTokenInstance']}"
            response = requests.request("GET", url, headers=headers, data=payload)

        elif request.form['action'] == 'sendMessage':
            # Create the URL to create the request
            url = f"{credentials['apiUrl']}/waInstance{credentials['idInstance']}/sendMessage/{credentials['apiTokenInstance']}"
            payload = {
                "chatId": "5491133717702@c.us",
                "message": credentials['message']
            }
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(url, json=payload, headers=headers)

        elif request.form['action'] == 'sendFileByUrl':
             # Create the URL to create the request
            url = f"{credentials['apiUrl']}/waInstance{credentials['idInstance']}/sendFileByUrl/{credentials['apiTokenInstance']}"
            payload = {
                "chatId": f"{credentials['phone']}@c.us", 
                "urlFile":f"{credentials['urlFile']}", 
                "fileName": "greenapi.png", 
                "caption": "logo"
            }
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(url, json=payload)

        return render_template('index.html', data=response.json())
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()