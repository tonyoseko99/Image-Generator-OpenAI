from django import forms


class ImageForm(forms.Form):
    prompt = forms.CharField(label='Prompt', max_length=100,
                             widget=forms.TextInput(attrs={'class': 'text-field'}))
    n = forms.IntegerField(label='Number of images',
                           widget=forms.NumberInput(attrs={'class': 'integer-field'}))
    size = forms.CharField(label='Size', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'text-field'}))
