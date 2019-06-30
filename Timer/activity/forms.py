from django import forms
from .models import Activities


class ActivityForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),
                           label='Enter the date')

    class Meta:
        model = Activities
        fields = ('activity', 'date', 'duration')


class ActivityEditForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),
                           label='Enter the date')

    class Meta:
        model = Activities
        fields = ('activity', 'date', 'duration')
