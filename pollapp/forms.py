from django import forms
from django.forms import ModelForm
from pollapp.models import *

class PollForm(forms.ModelForm):

    class Meta:
        model = Polldata
        fields = ['question','option1','option2','option3']