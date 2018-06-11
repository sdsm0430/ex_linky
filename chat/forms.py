from django import forms
from linky.models import Review

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Review
        fields = ('review',)