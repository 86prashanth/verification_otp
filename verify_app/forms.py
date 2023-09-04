from django import forms 
from code_.models import Code


class CodeForm(forms.ModelForm):
    number=forms.CharField(label='code',help_text="enter sms verification..")
    class Meta:
        model=Code 
        fields=('number',)