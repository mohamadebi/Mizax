from django import forms
from .models import Place


class PlaceForm( forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    ticket_price = forms.IntegerField()
    opentime = forms.DateTimeField(required=False)


class PlaceUpdateForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name','city','ticket_price')

class PlacedeleteForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name','city','ticket_price')
