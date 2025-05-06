from django.contrib import admin
from .models import (
    ErishilganYutuqlar, ErishilganYutuqRasmlari,
    MatbuotXizmati, MatbuotXizmatiRasmlar,
    ElonVaTadbirlar, ElonVaTadbirlarRasmlar,
    Murojat, MurojatHammuallif,
    BoShIshOrin, Rahbariyat, BoshqarmaTarixi, QabulJadvali
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
    search_fields = ('title_uz', 'content_uz')
    list_filter = ('created_at', 'updated_at')
    inlines = [ErishilganYutuqRasmlariInline]
    fields = ('title_uz', 'image', 'content_uz', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

# Inline for Matbuot Xizmati
class MatbuotXizmatiRasmlarInline(admin.TabularInline):
    model = MatbuotXizmatiRasmlar
    extra = 1
    verbose_name = "Yangilik Rasmi"
    verbose_name_plural = "Yangilik Rasmlari"

@admin.register(MatbuotXizmati)
class MatbuotXizmatiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title_uz', 'content_uz')
    list_filter = ('created_at', 'updated_at')
    inlines = [MatbuotXizmatiRasmlarInline]
    fields = ('title_uz', 'image', 'content_uz', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

# Inline for Elon va Tadbirlar
class ElonVaTadbirlarRasmlarInline(admin.TabularInline):
    model = ElonVaTadbirlarRasmlar
    extra = 1
    verbose_name = "Elon yoki Tadbir Rasmi"
    verbose_name_plural = "Elon va Tadbir Rasmlari"

@admin.register(ElonVaTadbirlar)
class ElonVaTadbirlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title_uz', 'content_uz')
    list_filter = ('created_at', 'updated_at')
    inlines = [ElonVaTadbirlarRasmlarInline]
    fields = ('title_uz', 'image', 'content_uz', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

# Inline for Boshqarma Haqida
class BoShIshOrinInline(admin.TabularInline):
    model = BoShIshOrin
    extra = 1
    verbose_name = "Bosh ish o'rinlari"
    verbose_name_plural = "Bosh ish o'rinlari"
    fields = ('image', 'lavozim_uz', 'joylashuv_uz', 'sana', 'tavsif_uz')

class RahbariyatInline(admin.TabularInline):
    model = Rahbariyat
    extra = 1
    verbose_name = "Rahbariyat"
    verbose_name_plural = "Rahbariyatlar"
    fields = ('ism_uz', 'image', 'lavozim_uz', 'telefon', 'email')

@admin.register(QabulJadvali)
class QabulJadvaliAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name_uz',)
    list_filter = ('name_uz',)
    fields = ('name_uz', 'matn_uz', 'image')

@admin.register(BoshqarmaTarixi)
class BoshqarmaTarixiAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title_uz', 'content_uz')
    list_filter = ('created_at', 'title_uz')
    inlines = [BoShIshOrinInline, RahbariyatInline]
    fields = ('image', 'title_uz', 'content_uz', 'created_at')
    readonly_fields = ('created_at',)

# Inline for Murojat
class MurojatHammuallifInline(admin.TabularInline):
    model = MurojatHammuallif
    extra = 1
    verbose_name = "MurojatHammuallif"
    verbose_name_plural = "MurojatHammualliflar"
    fields = ('familya_uz', 'ismi_uz', 'otasining_ismi', 'pochta_manzil')

@admin.register(Murojat)
class MurojatAdmin(admin.ModelAdmin):
    list_display = ('murojat_kimga', 'create_date', 'ismi', 'familiya', 'id')
    search_fields = ('ismi_uz', 'familiya_uz', 'murojat_kimga')
    list_filter = ('murojat_kimga', 'murojat_turi', 'create_date')
    inlines = [MurojatHammuallifInline]
    fields = (
        'murojat_kimga', 'murojat_turi', 'familiya_uz', 'ismi_uz', 'otasining_ismi',
        'kompaniyaning_nomi', 'boglanish_malumotlari', 'pochta_manzil',
        'mirojat_matni_uz', 'hujjatlar', 'tel_raqam', 'create_date'
    )
    readonly_fields = ('create_date',)
    list_per_page = 20