import os
import pandas as pd
import PyPDF2
import re

class helpLineNumber:
    def __init__(self):
        pass
    def get_help_numbers(self,req):
        self.req= req
        sessionID= req.get('responseID')
        result = req.get("queryResult")
        #intent = result.get("intent").get('displayName')
        #log.write_log(sessionID, "User Says: "+user_says)


        #if(intent=='cases'):
        parameters = result.get("parameters")
        city = parameters.get("city_name")
        pattern= city+'\s\d+\s'
        pdffileobj = open('helpline.pdf', 'rb')
        pdfreader = PyPDF2.PdfFileReader(pdffileobj)
        x = pdfreader.numPages
        pageobj = pdfreader.getPage(0)
        text = pageobj.extractText()
        text= text.replace('\n','')
        text=text.replace('-','')
        number= re.findall(pattern,text)
        detail_list=number[0].split(' ')
        fulfillmentText= 'Helpline number for {} is {} and the central Helpline number is +91-11-23978046'.format(detail_list[0],detail_list[1])
        return {
            'fulfillmentText': fulfillmentText,
            'source': fulfillmentText
        }

