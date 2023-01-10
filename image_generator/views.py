import os
import openai
import requests

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ImageForm

# use the os.getenv() function to reference the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_image(request):
    # Generate the image
    response = openai.Image.create(
        prompt="a white siamese cat",
        n=1,
        size="1024x1024"
    )

    image_url = response['data'][0]['url']
   # Get the image URL from the response
    print(image_url)

    # render the image in the browser
    return render(request, 'index.html', {'image_url': image_url})

# view to handle form submission and validation
def input_form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
