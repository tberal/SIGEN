import json
import requests
import datetime

from flask import render_template, request
from wtforms import FormField, StringField
from flask.views import View

from werkzeug import secure_filename

from SIGEN.forms import ReceituarioHeader, ReceituarioItem
from SIGEN.configs import envs, urls, plants, tecnicos, receituario
from SIGEN.functions import UpdateFile

class MapView(View):
    """
    Main page, doesn't require a logged user. Loads a form for cpf search. Upon
    searching will also load a list with debts from the given cpf

    Returns:
        Loads the index page with the search results if successful or with 
        just the form if the search is empty
    """
    methods = ['GET', 'POST']
    def dispatch_request(self):
        for k, v in receituario['header'].items():
            setattr(ReceituarioHeader, k, StringField(label=k, default=v))

        for k, v in receituario['item'].items():
            setattr(ReceituarioItem, k, StringField(label=k, default=v))

        form = ReceituarioHeader()
        
        if form.validate_on_submit():
            print(form.data)
            return render_template('map.html', form=form)
        return render_template('map.html', form=form)
