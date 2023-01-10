import os
import openai
import requests

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageForm

# set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# use the os.getenv() function to reference the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def handle_form_submission(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            # get the data from the form
            prompt = form.cleaned_data['prompt']
            n = form.cleaned_data['n']
            size = form.cleaned_data['size']

            # Use the data from the form to generate the image
            response = openai.Image.create(
                prompt=prompt,
                n=n,
                size=size
            )

            image_url = response['data'][0]['url']

            # render the image in the browser
            return render(request, 'form.html', {'image_url': image_url})
    else:
        form = ImageForm()

    return render(request, 'form.html', {'form': form})