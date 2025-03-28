from django.shortcuts import render, get_object_or_404

from news_app.models import ErishilganYutuqlar, MatbuotXizmati, ElonVaTadbirlar

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

    ctx = {
        'data': matbuot_xizmati,
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

def murojaatlar(request):
    return render(request, 'pages/murojaatlar.html')


