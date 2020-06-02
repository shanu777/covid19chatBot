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
from output.casese import get_facts

app =Flask(__name__)

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req= request.get_json(silent=True, force=True)
    result = get_facts()
    res= result.intent_matcher(req)

    res= json.dumps(res, indent=4)

    r= make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__=='__main__':
    app.run(debug=True)

