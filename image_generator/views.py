from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.
API_KEY = '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'

def image(request):
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={ 'Authorization': 'Bearer ' + API_KEY },
    )

