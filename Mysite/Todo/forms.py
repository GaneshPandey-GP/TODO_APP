from django import forms
from .models import TODO

class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Add Your Task Here.'}))

    class Meta:
        model = TODO
        fields = '__all__'