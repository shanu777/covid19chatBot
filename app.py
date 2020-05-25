from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import bs4

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

def processRequest(req):
    sessionID= req.get('responseID')
    result = req.get("queryResult")
    user_says=result.get("queryText")
    #log.write_log(sessionID, "User Says: "+user_says)
    parameters = result.get("parameters")
    city=parameters.get("city_name")

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
                    fullfilmentText=('cases: ' + data[x][2])
                    return {'fullfilmentText':fullfilmentText}
                else:
                    continue

            else:
                continue



if __name__=='__main__':
    app.run(debug=True)