from django import forms

class ImageForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=100)
    n = forms.IntegerField(label='Number of images')
    size = forms.CharField(label='Image size', max_length=100)