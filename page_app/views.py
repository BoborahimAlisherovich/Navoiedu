from django.shortcuts import render, get_object_or_404, redirect
from news_app.models import (
    ErishilganYutuqlar, 
    MatbuotXizmati, 
    ElonVaTadbirlar,
    BoShIshOrin,
    Rahbariyat,
    BoshqarmaTarixi,
    QabulJadvali,
    MatbuotXizmatiRasmlar,
)
from news_app.forms import MurojatForm, MurojatHammuallifForm
from django.forms import formset_factory
from news_app.bot import send_message

def home_page(request):
    elon_va_tadbirlar = ElonVaTadbirlar.objects.all()
    bosh_ish_urinlar = BoShIshOrin.objects.all()

    ctx = {
        'elon_va_tadbirlar': elon_va_tadbirlar,
        'bosh_ish_urinlar': bosh_ish_urinlar,
    }

    return render(request, 'home.html', ctx)

def korrupsiya(request):
    return render(request, 'pages/korrupsiya.html')

def erishilgan_yutuqlar(request):
    erishilgan_yutuqlar = ErishilganYutuqlar.objects.all()

    ctx = {
        'erishilgan_yutuqlar': erishilgan_yutuqlar,
    }

    return render(request, 'pages/erishilgan-yutuqlar.html', ctx)

def qabul_jadvali(request):
    qabul_jadvali = QabulJadvali.objects.all()

    ctx = {
        'qabul_jadvali': qabul_jadvali,
    }

    return render(request, 'pages/qabul_jadvali.html', ctx)

def qabul_jadvali_detail(request, pk):
    jadvallar = get_object_or_404(QabulJadvali, pk=pk)
    jadvallar.view_count = jadvallar.view_count + 1
    jadvallar.save()

    ctx = {
        'data': jadvallar,
    }
    return render(request, 'pages/news_detail.html', ctx)

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
    rahbariyatlar.view_count = rahbariyatlar.view_count + 1
    rahbariyatlar.save()

    ctx = {
        'data': rahbariyatlar,
    }
    return render(request, 'pages/news_detail.html', ctx)

def bosh_ish_urinlar_detail(request, pk):
    bosh_ish_urin = get_object_or_404(BoShIshOrin, pk=pk)
    bosh_ish_urin.view_count = bosh_ish_urin.view_count + 1
    bosh_ish_urin.save()

    ctx = {
        'data': bosh_ish_urin,
    }
    return render(request, 'pages/news_detail.html', ctx)

def erishilgan_yutuq_detail(request, pk):
    erishilgan_yutuq = get_object_or_404(ErishilganYutuqlar, pk=pk)
    erishilgan_yutuq.view_count = erishilgan_yutuq.view_count + 1
    erishilgan_yutuq.save()

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
    matbuot_xizmati.view_count = matbuot_xizmati.view_count + 1
    matbuot_xizmati.save()
    rasmlar = MatbuotXizmatiRasmlar.objects.filter(yutuq=matbuot_xizmati)

    ctx = {
        'data': matbuot_xizmati,
        'rasmlar': rasmlar,
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
    elon_va_tadbir.view_count = elon_va_tadbir.view_count + 1
    elon_va_tadbir.save()

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

def boshqarma_haqida(request):
    boshqarma_haqida = BoshqarmaTarixi.objects.all()

    ctx = {
        'boshqarma_haqida': boshqarma_haqida,
    }

    return render(request, 'pages/boshqarma-haqida.html', ctx)

def boshqarma_haqida_detail(request, pk):
    boshqarma_haqid = get_object_or_404(BoshqarmaTarixi, pk=pk)
    boshqarma_haqid.view_count = boshqarma_haqid.view_count + 1
    boshqarma_haqid.save()

    ctx = {
        'data': boshqarma_haqid,
    }

    return render(request, 'pages/news_detail.html', ctx)

def murojaatlar(request):
    HammuallifFormSet = formset_factory(MurojatHammuallifForm, extra=0)

    if request.method == 'POST':
        form = MurojatForm(request.POST, request.FILES)
        formset = HammuallifFormSet(request.POST, prefix='hammuallif')

        if form.is_valid():
            murojat = form.save()

            send_message(
                murojat_kimga=murojat.murojat_kimga,
                murojat_turi=murojat.murojat_turi,
                familiya=murojat.familiya,
                ismi=murojat.ismi,
                otasining_ismi=murojat.otasining_ismi,
                kompaniyaning_nomi=murojat.kompaniyaning_nomi,
                pochta_manzil=murojat.pochta_manzil,
                mirojat_matni=murojat.mirojat_matni,
                tel_raqam=murojat.tel_raqam,
                create_date=murojat.create_date,
                id=murojat.id
            )

            if formset.is_valid():
                for hammuallif_form in formset:
                    if hammuallif_form.cleaned_data:
                        hammuallif = hammuallif_form.save(commit=False)
                        hammuallif.murojat = murojat
                        hammuallif.save()

            return redirect('home_page')
    else:
        form = MurojatForm()
        formset = HammuallifFormSet(prefix='hammuallif')

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'pages/murojaatlar.html', context)