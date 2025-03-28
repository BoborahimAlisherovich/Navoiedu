from django.contrib import admin
from .models import (
    ErishilganYutuqlar,
    ErishilganYutuqRasmlari,
    MatbuotXizmati,
    MatbuotXizmatiRasmlar,
    ElonVaTadbirlar,
    ElonVaTadbirlarRasmlar
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
