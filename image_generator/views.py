import os
import openai
import requests
from django.http import JsonResponse

# set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "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"

# use the os.getenv() function to reference the API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_image(request):
    # Get the prompt from the request
    prompt = "This is a picture of a dog."
    # Generate the image
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\ Image URL:"],
    )
    # Get the image URL from the response
    image_url = response["choices"][0]["text"].split("Image URL: ")[1].strip()
    # Return the image URL
    return JsonResponse({"image_url": image_url})
