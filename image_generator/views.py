from django.shortcuts import render
from django.http import HttpResponse

import requests
import os
import openai


# Create your views here.
API_KEY = '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'


def image(request):
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + API_KEY
        },
        json={
            "model": "text-davinci-003",
            "prompt": "this is a test",
            "temperature": 0,
            "max_tokens": 7
        }
    )
