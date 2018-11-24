import json
import random

import requests
from flask import Flask, request, Response
from flask_cors import CORS

answers = {
    1: 'triplets',
    2: 'monopoly',
    3: '20',
    4: 'numbers',
    5: 'all boys',
    6: 'what'
}

winners = []

app = Flask(__name__)
CORS(app)

@app.route("/check-answer", methods=["GET"])
def checkAnswer():
    index  = int(request.args.get('index'))
    answer = str(request.args.get('answer'))
    key = str(request.headers['secret'])
    if(key != "angular"):
        return 'false'
    else:
        return str(answer.lower() == answers[index].lower()).lower()

@app.route("/save", methods=["GET"])
def saveEmail():
    email = request.args.get('email')
    print("NEW EMAIL: " + email)
    winners.append(email)
    return json.dumps("success")

@app.route('/winners',methods=["GET"])
def getEmails():
    return json.dumps(winners)

if __name__ == "__main__":
    app.run(host="127.0.0.1",port="8080")