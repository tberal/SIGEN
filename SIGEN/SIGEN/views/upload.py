import json
import requests
import datetime

from flask import render_template, request
from flask.views import View

from werkzeug import secure_filename

from SIGEN.forms import UploadFile
from SIGEN.configs import envs, urls, plants, tecnicos
from SIGEN.functions import Build, Send

class UploadView(View):
    """
    Main page, doesn't require a logged user. Loads a form for cpf search. Upon
    searching will also load a list with debts from the given cpf

    Returns:
        Loads the index page with the search results if successful or with 
        just the form if the search is empty
    """
    methods = ['GET', 'POST']
    def dispatch_request(self):
        form = UploadFile()
        if form.validate_on_submit():
            fileName = form.file.data.filename
            fileData = request.files['file']
            plant = form.data['plant']
            ftype = form.data['filetype']
            env = envs[form.data['env']]

            whList = [line.split(';') for line in fileData.read().decode('ISO-8859-1').splitlines()]

            msgs = Build(ftype, whList)
                        
            responses = Send(env, plant, ftype, msgs)
                    
            return render_template('upload.html', form=form, results=responses)
        return render_template('upload.html', form=form, results=None)
