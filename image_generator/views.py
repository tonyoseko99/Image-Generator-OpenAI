from django.shortcuts import render

import requests
import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")


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
            "model": "image-alpha-001",
            "prompt": "A cute baby sea otter wearing a beret",
            "n": 2,
            "size": "1024x1024",
            'response_format': 'url'
        }
        image_url = response.json()['data'][0]['url']
        return render(request, 'myapp/image.html', {'image_url': image_url})
    )
