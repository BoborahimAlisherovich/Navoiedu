# news_app/forms.py
from django import forms
from .models import Murojat, MurojatHammuallif

class MurojatForm(forms.ModelForm):
    class Meta:
        model = Murojat
        fields = [
            'murojat_kimga', 'murojat_turi', 'familiya', 'ismi', 'otasining_ismi',
            'kompaniyaning_nomi', 'pochta_manzil', 'tel_raqam', 'mirojat_matni', 'hujjatlar'
        ]
        widgets = {
            'mirojat_matni': forms.Textarea(attrs={'rows': 5}),
        }

class MurojatHammuallifForm(forms.ModelForm):
    class Meta:
        model = MurojatHammuallif
        fields = ['familya', 'ismi', 'otasining_ismi', 'pochta_manzil']