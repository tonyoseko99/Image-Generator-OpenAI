import os
import openai
import requests
from django.http import JsonResponse

# set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

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
    JsonResponse({'image_url': image_url})

    # render the image in the browser
    return render(request, 'image_generator/templates/index.html', {'image_url': image_url})

