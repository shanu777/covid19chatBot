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
class count_cases:
    def __init__(self):
        pass
    def get_numbers(self,req):
        self.req= req
        sessionID= req.get('responseID')
        result = req.get("queryResult")
        #intent = result.get("intent").get('displayName')
        #log.write_log(sessionID, "User Says: "+user_says)


        #if(intent=='cases'):
        parameters = result.get("parameters")
        city = parameters.get("city_name")
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
                    text= str('Number of active cases: ' + data[x][2]+'\n Number of people who recovered: '+data[x][3]+'\n number of deaths: '+data[x][4]+'Total number of cases is:'+data[x][5])
                    return {
                        'fulfillmentText': text,
                        'source': text
                    }
                else:
                    continue

            else:
                continue