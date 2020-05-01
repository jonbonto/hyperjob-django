from django import forms

class NewResumeForm(forms.Form):
    description = forms.CharField(label='Description', max_length=1024, required=True)
