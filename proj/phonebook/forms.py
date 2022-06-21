from django import forms

from . import models

class CreatePersoneForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.Textarea(), help_text='Separated by new line')
    class Meta:
        model = models.Persone
        fields = ('name', 'phones')