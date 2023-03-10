import os
import openai
import requests

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ImageForm

# set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = ""

# use the os.getenv() function to reference the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def handle_form_submission(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            # get the data from the form
            prompt = form.cleaned_data['prompt']
            n_images = form.cleaned_data['n']
            size = form.cleaned_data['size']

            # Use the data from the form to generate the image
            response = openai.Image.create(
                prompt=prompt,
                n=n_images,
                size=size
            )

            image_urls = [image['url'] for image in response['data']]
            # print the image URLs to the console for debugging
            print(image_urls)
            # print the number of objects in the response to the console for debugging
            print(len(response['data']))

            # render the image in the browser
            return render(request, 'form.html', {'image_urls': image_urls})
    else:
        form = ImageForm()

    return render(request, 'form.html', {'form': form})
