from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),

    path('boshqarma-haqida/', boshqarma_haqida, name='boshqarma_haqida'),
    path('boshqarma-haqida/<int:pk>/', boshqarma_haqida_detail, name='boshqarma_haqida_detail'),
    
    path('boshqarma-haqida/erishilgan-yutuqlar/', erishilgan_yutuqlar),
    path('boshqarma-haqida/erishilgan-yutuqlar/<int:pk>/', erishilgan_yutuq_detail, name='erishilgan_yutuq_detail'),

    path('matbuot-xizmati/', matbuot_xizmati),
    path('matbuot_xizmati/<int:pk>/', matbuot_xizmati_detail, name='matbuot_xizmati_detail'),

    path('matbuot-xizmati/elon-va-tadbirlar/', elon_va_tadbirlar),
    path('matbuot-xizmati/elon-va-tadbirlar/<int:pk>/', elon_va_tadbir_detail, name='elon_va_tadbir_detail'),

    path('matbuot-xizmati/yangiliklar/', yangiliklar),
    path('murojaat_izlash/', murojaat_izlash),
    # path('murojaatlar/', murojaatlar),

    path('boshqarma-haqida/ish-urin/', bosh_ish_urinlar),
    path('boshqarma-haqida/ish-urin/<int:pk>/', bosh_ish_urinlar_detail, name='bosh_ish_urinlar_detail'),

    path('boshqarma-haqida/rahbariyat/', rahbariyat),
    path('boshqarma-haqida/rahbariyat/<int:pk>/', rahbariyat_detail, name='rahbariyat_detail'),
    
    path('boshqarma-haqida/murojaatlar/', murojaatlar),
    # path('boshqarma-haqida/murojaatlar/<int:pk>/', rahbariyat_detail, name='rahbariyat_detail'),

     path('boshqarma-haqida/qabul-jadvali/', qabul_jadvali),
     path('boshqarma-haqida/qabul-jadvali/<int:pk>/', qabul_jadvali_detail, name='qabul_jadvali_detail'),
    
    path('korrupsiyaga-qarshi-kurashish/',korrupsiya),
    path('murojaatlar/',murojaatlar),



]
