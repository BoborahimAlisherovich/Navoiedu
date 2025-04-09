from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns  # 👈 Qo‘shildi

# Static settings
from django.conf import settings
from django.conf.urls.static import static

# Admin custom
admin.site.site_title = "Admin"
admin.site.site_header = "Admin panel"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 🌐 Tilni qo‘llab-quvvatlovchi URL-lar
urlpatterns += i18n_patterns(
    path('', include('page_app.urls')),
)

# Static va media fayllar uchun
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
