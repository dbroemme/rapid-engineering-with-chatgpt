# forms.py
from django import forms

class QuizForm(forms.Form):
    topic = forms.CharField(max_length=100)
    num_questions = forms.IntegerField(min_value=1)

class ScreenNameForm(forms.Form):
    screen_name = forms.CharField(label='Screen Name', max_length=100)
