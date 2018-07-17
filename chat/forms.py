from django import forms
from linky.models import Review, Musical, Apply

class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Musical
        fields = ('password',)
        exclude = (
        'title', 'published_date', 'producer', 'producer_logo', 'term', 'place', 'slogan', 'genre', 'viewing_age',
        'runtime', 'language', 'poster', 'banner_image', 'background_image', 'repre_image', 'csv', 'admin_password',
        'admin_password2',
        )

class AdminPasswordForm(forms.ModelForm):
    admin_password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Musical
        fields = ('admin_password2',)
        exclude = (
        'title', 'published_date', 'producer', 'producer_logo', 'term', 'place', 'slogan', 'genre', 'viewing_age',
        'runtime', 'language', 'poster', 'banner_image', 'background_image', 'repre_image', 'csv', 'password',
        'admin_password',
        )


class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Review
        fields = ('review',)

class ApplyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    date = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    personnel = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Apply
        fields = ('name', 'phone', 'date', 'personnel', )
        exclude = ('ticket_image',)

class ApplyImageForm(forms.ModelForm):
    ticket_image = forms.ImageField()

    class Meta:
        model = Apply
        fields = ('ticket_image',)
        exclude = ('name', 'phone', 'date', 'personnel', )