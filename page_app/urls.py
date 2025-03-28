from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home_page'),

    path('boshqarma-haqida/', boshqarma_haqida),

    path('boshqarma-haqida/erishilgan-yutuqlar/', erishilgan_yutuqlar),
    path('boshqarma-haqida/erishilgan-yutuqlar/<int:pk>/', erishilgan_yutuq_detail, name='erishilgan_yutuq_detail'),

    path('matbuot-xizmati/', matbuot_xizmati),
    path('matbuot_xizmati/<int:pk>/', matbuot_xizmati_detail, name='matbuot_xizmati_detail'),

    path('matbuot-xizmati/elon-va-tadbirlar/', elon_va_tadbirlar),
    path('matbuot-xizmati/elon-va-tadbirlar/<int:pk>/', elon_va_tadbir_detail, name='elon_va_tadbir_detail'),

    path('matbuot-xizmati/yangiliklar/', yangiliklar),
    path('murojaat_izlash/', murojaat_izlash),
    path('murojaatlar/', murojaatlar),

]
