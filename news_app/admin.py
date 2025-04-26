from django.contrib import admin
from .models import (
    ErishilganYutuqlar,
    ErishilganYutuqRasmlari,
    MatbuotXizmati,
    MatbuotXizmatiRasmlar,
    ElonVaTadbirlar,
    ElonVaTadbirlarRasmlar,

    Murojat,
    MurojatHammuallif,    
    

    #boshqarma haqida 
    BoShIshOrin,
    Rahbariyat,
    BoshqarmaTarixi,
    QabulJadvali,
  
    #narmativ hujatlar

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
    verbose_name = "Yangilik Rasmi"
    verbose_name_plural = "yangilik Rasmlari"

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


# class QabulJadvaliInline(admin.TabularInline):
#     model = QabulJadvali
#     extra = 1
#     verbose_name = "QabulJadvali"
#     verbose_name_plural = "QabulJadvalilar"

@admin.register(QabulJadvali)
class QabulJadvaliAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name', )
    list_filter = ('name',)

@admin.register(BoshqarmaTarixi)
class BoshqarmaTarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at','title')
    inlines = [BoShIshOrinInline,RahbariyatInline]


class MurojatHammuallifInline(admin.TabularInline):
    model = MurojatHammuallif
    extra = 1
    verbose_name = "MurojatHammuallif"
    verbose_name_plural = "MurojatHammualliflar"



# @admin.register(Murojat)
# class MurojatAdmin(admin.ModelAdmin):
#     list_display = ('id', 'murojat_kimga', 'create_date','ismi')
#     search_fields = ('ismi', 'murojat_kimga')
#     list_filter = ('murojat_kimga','ismi')
#     inlines = [MurojatHammuallifInline]
    

@admin.register(Murojat)
class MurojatAdmin(admin.ModelAdmin):
    list_display = ('murojat_kimga', 'create_date', 'ismi', 'familiya','id')
    search_fields = ('ismi', 'familiya', 'murojat_kimga')
    list_filter = ('murojat_kimga', 'murojat_turi', 'create_date')
    inlines = [MurojatHammuallifInline]
    readonly_fields = ('create_date',)
    list_per_page = 20
