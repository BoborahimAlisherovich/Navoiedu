from django.contrib import admin
from .models import (
    ErishilganYutuqlar,
    ErishilganYutuqRasmlari,
    MatbuotXizmati,
    MatbuotXizmatiRasmlar,
    ElonVaTadbirlar,
    ElonVaTadbirlarRasmlar,

    #boshqarma haqida 
    BoShIshOrin,
    Rahbariyat,
    BoshqarmaTarixi,
    QabulJadvali,
  
    #narmativ hujatlar

    OzbekistonQonunlari,
    PrezidentFarmonlari,
    OliyTalImFanInnovatsiya,
    ViloyatQarorlari,
    OzKuchiniYoqotgan
    
)

# Inline for Erishilgan Yutuqlar
class ErishilganYutuqRasmlariInline(admin.TabularInline):
    model = ErishilganYutuqRasmlari
    extra = 1
    verbose_name = "Yutuq Rasmi"
    verbose_name_plural = "Yutuq Rasmlari"

@admin.register(ErishilganYutuqlar)
class ErishilganYutuqlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    inlines = [ErishilganYutuqRasmlariInline]

# Inline for Matbuot Xizmati
class MatbuotXizmatiRasmlarInline(admin.TabularInline):
    model = MatbuotXizmatiRasmlar
    extra = 1
    verbose_name = "Matbuot Rasmi"
    verbose_name_plural = "Matbuot Rasmlari"

@admin.register(MatbuotXizmati)
class MatbuotXizmatiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    inlines = [MatbuotXizmatiRasmlarInline]

# Inline for Elon va Tadbirlar
class ElonVaTadbirlarRasmlarInline(admin.TabularInline):
    model = ElonVaTadbirlarRasmlar
    extra = 1
    verbose_name = "Elon yoki Tadbir Rasmi"
    verbose_name_plural = "Elon va Tadbir Rasmlari"

@admin.register(ElonVaTadbirlar)
class ElonVaTadbirlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at')
    inlines = [ElonVaTadbirlarRasmlarInline]


#-------------yangi ---------------

class BoShIshOrinInline(admin.TabularInline):
    model = BoShIshOrin
    extra = 1
    verbose_name = "Bosh ish o'rinlari"
    verbose_name_plural = "Bosh ish o'rinlari"

class RahbariyatInline(admin.TabularInline):
    model = Rahbariyat
    extra = 1
    verbose_name = "Rahbariyat"
    verbose_name_plural = "Rahbariyatlar"


class QabulJadvaliInline(admin.TabularInline):
    model = QabulJadvali
    extra = 1
    verbose_name = "QabulJadvali"
    verbose_name_plural = "QabulJadvalilar"


@admin.register(BoshqarmaTarixi)
class BoshqarmaTarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at','title')
    inlines = [BoShIshOrinInline,RahbariyatInline,QabulJadvaliInline]




#---------Normativ hujjatlar

class PrezidentFarmonlariInline(admin.TabularInline):
    model = PrezidentFarmonlari
    extra = 1
    verbose_name = "PrezidentFarmonlari"
    verbose_name_plural = "PrezidentFarmonlarilar"

class OliyTalImFanInnovatsiyaInline(admin.TabularInline):
    model = OliyTalImFanInnovatsiya
    extra = 1
    verbose_name = "OliyTalImFanInnovatsiya"
    verbose_name_plural = "OliyTalImFanInnovatsiyalar"

class ViloyatQarorlariInline(admin.TabularInline):
    model = ViloyatQarorlari
    extra = 1
    verbose_name = "ViloyatQarorlari"
    verbose_name_plural = "ViloyatQarorlarilar"


class OzKuchiniYoqotganInline(admin.TabularInline):
    model = OzKuchiniYoqotgan
    extra = 1
    verbose_name = "OzKuchiniYoqotgan"
    verbose_name_plural = "OzKuchiniYoqotganlar"


@admin.register(OzbekistonQonunlari)
class OzbekistonQonunlariAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'fayl', 'sana')
    search_fields = ('nomi', 'sana')
    list_filter = ('nomi','fayl')
    inlines = [PrezidentFarmonlariInline,OliyTalImFanInnovatsiyaInline,ViloyatQarorlariInline,OzKuchiniYoqotganInline]

