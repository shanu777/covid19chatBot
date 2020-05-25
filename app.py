from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import bs4
import os
from flask import make_response
import json
import bs4
from bs4 import BeautifulSoup
import requests

app =Flask(__name__)

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req= request.get_json(silent=True, force=True)
    res= processRequest(req)

    res= json.dumps(res, indent=4)

    r= make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
@app.route('/static_reply', methods=['POST'])
def static_reply():
    speech = "Hello there, this reply is from the webhook !! "
    string = "You are awesome !!"
    Message = "this is the message"

    my_result = {

        "fulfillmentText": string,
        "source": string
    }

    res = json.dumps(my_result, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def processRequest(req):
    sessionID= req.get('responseID')
    result = req.get("queryResult")
    user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    city=parameters.get("city_name")
    intent= result.get("intent").get('displayName')
    if(intent=='cases'):
        source = requests.get('https://www.mohfw.gov.in/').content
        soup = BeautifulSoup(source, 'lxml')
        rows = soup.find_all('tr')
        data = []
        for tr in rows:
            td = tr.find_all('td')
            data.append([i.text for i in td])
        data = data[0:-6]

        for x in range(len(data)):
            if len(data[x]) != 0:
                if data[x][1] == city:
                    text= str('cases: ' + data[x][2])
                    return {
                        'fulfillmentText': text,
                        'source': text
                    }
                else:
                    continue

            else:
                continue



if __name__=='__main__':
    port = int(os.getenv('PORT', 80))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')