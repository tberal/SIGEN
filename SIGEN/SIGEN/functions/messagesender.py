import json
import requests
import datetime

from flask import render_template, request
from flask.views import View

from werkzeug import secure_filename

from SIGEN.forms import UploadFile
from SIGEN.configs import envs, urls, plants, tecnicos

def Login(env, token):
    auth = json.loads(requests.post(url = env + urls['login'] + token, data = {},verify=False).content)
    return auth

def Submit(env, url, msg, headers, cookie):
    response = requests.post(url = env + url, data=json.dumps(msg), verify=False, headers=headers, cookies=cookie)
    return response

def Send(env, plant, ftype, msgs):
    responses = []
    
    headers = {
        'Disable-Cache': '_dc='+datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'),
        'Content-Type': 'application/json; charset=utf-8',
                }
    
    if ftype == 'R':
        for msg in msgs:
            user = Login(env, tecnicos[msg['creaSC']])
            cookie = {
                'SessionID': user['SessionID'],
                'UserAuth': user['UserAuth']
                }

            response = Submit(env, urls['rec'], msg, headers, cookie)

            if json.loads(response.content).get('Data').get('Msg', None) is not None:
                mensagem = json.loads(response.content)['Data']['Msg'][0]
            else:
                mensagem = 'Receituário ' + str(json.loads(response.content)['Data']['IdReceituario']) + ' criado.'
            responses.append(mensagem)
    else:
        user = Login(env, plants[plant]['token'])

        for msg in msgs:
            cookie = {
                'SessionID': user['SessionID'],
                'UserAuth': user['UserAuth']
                }

            response = Submit(env, urls['mov'], msg, headers, cookie)

            responses.append(json.loads(response.content)['Msg'][0])
                    
    return responses
