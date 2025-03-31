from django.shortcuts import render, get_object_or_404

from news_app.models import (
    ErishilganYutuqlar, 
    MatbuotXizmati, 
    ElonVaTadbirlar,
     BoShIshOrin,
    Rahbariyat,
    BoshqarmaTarixi,
    QabulJadvali,
    MatbuotXizmatiRasmlar,
  
    #narmativ hujatlar

    OzbekistonQonunlari,
    PrezidentFarmonlari,
    OliyTalImFanInnovatsiya,
    ViloyatQarorlari,
    OzKuchiniYoqotgan  )

# 93 311 16 01 

def home_page(request):
    elon_va_tadbirlar = ElonVaTadbirlar.objects.all()

    ctx = {
        'elon_va_tadbirlar': elon_va_tadbirlar
    }

    return render(request, 'home.html', ctx)



def boshqarma_haqida(request):
    return render(request, 'pages/boshqarma-haqida.html')




def erishilgan_yutuqlar(request):
    erishilgan_yutuqlar = ErishilganYutuqlar.objects.all()

    ctx = {
        'erishilgan_yutuqlar': erishilgan_yutuqlar,
    }

    return render(request, 'pages/erishilgan-yutuqlar.html', ctx)


def bosh_ish_urinlar(request):
    bosh_ish_urinlar = BoShIshOrin.objects.all()

    ctx = {
        'bosh_ish_urinlar': bosh_ish_urinlar,
    }

    return render(request, 'pages/ish-urin.html', ctx)


def rahbariyat(request):
    rahbariyat = Rahbariyat.objects.all()

    ctx = {
        'rahbariyat': rahbariyat,
    }

    return render(request, 'pages/rahbaryat.html', ctx)


def rahbariyat_detail(request, pk):
    rahbariyatlar = get_object_or_404(Rahbariyat, pk=pk)

    ctx = {
        'data': rahbariyatlar,
    }
    return render(request, 'pages/news_detail.html', ctx)

    


def bosh_ish_urinlar_detail(request, pk):
    bosh_ish_urin = get_object_or_404(BoShIshOrin, pk=pk)

    ctx = {
        'data': bosh_ish_urin,
    }
    return render(request, 'pages/news_detail.html', ctx)

    # return render(request, 'pages/ish-urin-detail.html', ctx)



def erishilgan_yutuq_detail(request, pk):
    erishilgan_yutuq = get_object_or_404(ErishilganYutuqlar, pk=pk)

    ctx = {
        'data': erishilgan_yutuq,
    }

    return render(request, 'pages/news_detail.html', ctx)

def matbuot_xizmati(request):
    matbuot_xizmatlari = MatbuotXizmati.objects.all()

    ctx = {
        'matbuot_xizmatlari': matbuot_xizmatlari
    }
    return render(request, 'pages/matbuot-xizmati.html', ctx)

def matbuot_xizmati_detail(request, pk):
    matbuot_xizmati = get_object_or_404(MatbuotXizmati, pk=pk)
    rasmlar = MatbuotXizmatiRasmlar.objects.filter(yutuq=matbuot_xizmati)  # Tegishli rasmlar olinmoqda


    ctx = {
        'data': matbuot_xizmati,
        'rasmlar': rasmlar,  # Rasmlarni kontekstga qo'shamiz
    }
    


    return render(request, 'pages/news_detail.html', ctx)

def elon_va_tadbirlar(request):
    elon_va_tadbirlar = ElonVaTadbirlar.objects.all()

    ctx = {
        'elon_va_tadbirlar': elon_va_tadbirlar
    }

    return render(request, 'pages/elon-va-tadbirlar.html', ctx)


def elon_va_tadbir_detail(request, pk):
    elon_va_tadbir = get_object_or_404(ElonVaTadbirlar, pk=pk)

    ctx = {
        'data': elon_va_tadbir
    }

    return render(request, 'pages/news_detail.html', ctx)

def yangiliklar(request):
    matbuot_xizmatlari = MatbuotXizmati.objects.all()

    ctx = {
        'matbuot_xizmatlari': matbuot_xizmatlari
    }
    return render(request, 'pages/yangiliklar.html', ctx)


def murojaat_izlash(request):
    return render(request, 'pages/murojaat-izlash.html')



from django.shortcuts import render, redirect
from news_app.forms import MurojatForm

def murojaatlar(request):
    if request.method == 'POST':
        form = MurojatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'pages/success.html')  # yuborilganidan so'ngki sahifa
    else:
        form = MurojatForm()
    return render(request, 'pages/murojaatlar.html', {'form': form})
