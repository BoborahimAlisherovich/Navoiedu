from django import forms
from .models import Murojat

class MurojatForm(forms.ModelForm):
    class Meta:
        model = Murojat
        fields = [
            'murojat_kimga', 'murojat_turi', 'familiya', 'ismi', 'otasining_ismi',
            'kompaniyaning_nomi', 'boglanish_malumotlari', 'pochta_manzil',
            'mirojat_matni', 'hujjatlar', 'tel_raqam'
        ]
        widgets = {
            'mirojat_matni': forms.Textarea(attrs={'rows': 5}),
        }
