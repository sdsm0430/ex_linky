from django import forms
from linky.models import TMWL_review

class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = TMWL_review
        fields = ('review',)