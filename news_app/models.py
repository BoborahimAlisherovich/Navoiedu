from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from googletrans import Translator

# Initialize translator
translator = Translator()

# Models for Erishilgan Yutuqlar
class ErishilganYutuqRasmlari(models.Model):
    image = models.ImageField(upload_to="yutuqlar/", verbose_name="Yutuq Rasmi")
    yutuq = models.ForeignKey(
        'ErishilganYutuqlar',
        related_name='rasmlar',
        on_delete=models.CASCADE,
        verbose_name="Tegishli Yutuq"
    )

    def __str__(self):
        return f"Rasm: {self.image.name}"

    class Meta:
        verbose_name = "Yutuq Rasmi"
        verbose_name_plural = "Yutuq Rasmlari"


class ErishilganYutuqlar(models.Model):
    title = models.CharField(max_length=455, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='yutuqlar/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-translate title and content if not provided
        if self.title_uz and not self.title_en:
            self.title_en = translator.translate(self.title_uz, src='uz', dest='en').text
        if self.title_uz and not self.title_ru:
            self.title_ru = translator.translate(self.title_uz, src='uz', dest='ru').text
        if self.content_uz and not self.content_en:
            self.content_en = translator.translate(self.content_uz, src='uz', dest='en').text
        if self.content_uz and not self.content_ru:
            self.content_ru = translator.translate(self.content_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Erishilgan Yutuq"
        verbose_name_plural = "Erishilgan Yutuqlar"
        ordering = ['-id']


# Models for Matbuot Xizmati
class MatbuotXizmatiRasmlar(models.Model):
    image = models.ImageField(upload_to="matbuot/", verbose_name="Matbuot Rasmi")
    yutuq = models.ForeignKey(
        'MatbuotXizmati',
        related_name='rasmlar',
        on_delete=models.CASCADE,
        verbose_name="Tegishli Matbuot"
    )

    def __str__(self):
        
        return f"Rasm: {self.image.name}"

    class Meta:
        verbose_name = "Yangiliklar Rasmi"
        verbose_name_plural = "Yangiliklar Rasmlari"


class MatbuotXizmati(models.Model):
    title = models.CharField(max_length=455, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='Images/matbuot/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title_uz and not self.title_en:
            self.title_en = translator.translate(self.title_uz, src='uz', dest='en').text
        if self.title_uz and not self.title_ru:
            self.title_ru = translator.translate(self.title_uz, src='uz', dest='ru').text
        if self.content_uz and not self.content_en:
            self.content_en = translator.translate(self.content_uz, src='uz', dest='en').text
        if self.content_uz and not self.content_ru:
            self.content_ru = translator.translate(self.content_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-id']


# Models for Elon va Tadbirlar
class ElonVaTadbirlarRasmlar(models.Model):
    image = models.ImageField(upload_to="Images/elon_va_tadbirlar/", verbose_name="Elon va Tadbir Rasmi")
    elon_tadbir = models.ForeignKey(
        'ElonVaTadbirlar',
        related_name='rasmlar',
        on_delete=models.CASCADE,
        verbose_name="Tegishli Elon yoki Tadbir"
    )

    def __str__(self):
        return f"Rasm: {self.image.name}"

    class Meta:
        verbose_name = "Elon va Tadbir Rasmi"
        verbose_name_plural = "Elon va Tadbir Rasmlari"


class ElonVaTadbirlar(models.Model):
    title = models.CharField(max_length=455, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='Images/elon_va_tadbirlar/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title_uz and not self.title_en:
            self.title_en = translator.translate(self.title_uz, src='uz', dest='en').text
        if self.title_uz and not self.title_ru:
            self.title_ru = translator.translate(self.title_uz, src='uz', dest='ru').text
        if self.content_uz and not self.content_en:
            self.content_en = translator.translate(self.content_uz, src='uz', dest='en').text
        if self.content_uz and not self.content_ru:
            self.content_ru = translator.translate(self.content_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Elon va Tadbir"
        verbose_name_plural = "Elon va Tadbirlar"
        ordering = ['-id']


# Models for Boshqarma Haqida
class BoShIshOrin(models.Model):
    image = models.ImageField(upload_to='Images/bo_shish_orin/', verbose_name="Rasm")
    lavozim = models.CharField(max_length=100)
    joylashuv = models.CharField(max_length=100)
    sana = models.DateField()
    tavsif = models.TextField()
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    boshqarma_tarix = models.ForeignKey(
        'BoshqarmaTarixi',
        related_name="BoShIshOrin",
        on_delete=models.CASCADE,
        verbose_name="Tegishli boshqarma tarix"
    )

    def __str__(self):
        return self.lavozim

    def save(self, *args, **kwargs):
        if self.lavozim_uz and not self.lavozim_en:
            self.lavozim_en = translator.translate(self.lavozim_uz, src='uz', dest='en').text
        if self.lavozim_uz and not self.lavozim_ru:
            self.lavozim_ru = translator.translate(self.lavozim_uz, src='uz', dest='ru').text
        if self.joylashuv_uz and not self.joylashuv_en:
            self.joylashuv_en = translator.translate(self.joylashuv_uz, src='uz', dest='en').text
        if self.joylashuv_uz and not self.joylashuv_ru:
            self.joylashuv_ru = translator.translate(self.joylashuv_uz, src='uz', dest='ru').text
        if self.tavsif_uz and not self.tavsif_en:
            self.tavsif_en = translator.translate(self.tavsif_uz, src='uz', dest='en').text
        if self.tavsif_uz and not self.tavsif_ru:
            self.tavsif_ru = translator.translate(self.tavsif_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)


class Rahbariyat(models.Model):
    ism = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/rahbariyat/', verbose_name="Rasm")
    lavozim = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")
    boshqarma_tarix = models.ForeignKey(
        'BoshqarmaTarixi',
        related_name="Rahbariyatlar",
        on_delete=models.CASCADE,
        verbose_name="Tegishli Rahbariyat"
    )

    def __str__(self):
        return self.ism

    def save(self, *args, **kwargs):
        if self.ism_uz and not self.ism_en:
            self.ism_en = translator.translate(self.ism_uz, src='uz', dest='en').text
        if self.ism_uz and not self.ism_ru:
            self.ism_ru = translator.translate(self.ism_uz, src='uz', dest='ru').text
        if self.lavozim_uz and not self.lavozim_en:
            self.lavozim_en = translator.translate(self.lavozim_uz, src='uz', dest='en').text
        if self.lavozim_uz and not self.lavozim_ru:
            self.lavozim_ru = translator.translate(self.lavozim_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)


class BoshqarmaTarixi(models.Model):
    image = models.ImageField(upload_to='Images/boshqarma_haqida/', verbose_name="Asosiy Rasm")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.title_uz and not self.title_en:
            self.title_en = translator.translate(self.title_uz, src='uz', dest='en').text
        if self.title_uz and not self.title_ru:
            self.title_ru = translator.translate(self.title_uz, src='uz', dest='ru').text
        if self.content_uz and not self.content_en:
            self.content_en = translator.translate(self.content_uz, src='uz', dest='en').text
        if self.content_uz and not self.content_ru:
            self.content_ru = translator.translate(self.content_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Boshqarma Haqida"
        verbose_name_plural = "Boshqarma Haqida"


class QabulJadvali(models.Model):
    name = models.CharField(max_length=255, verbose_name="Politexnikum nomi")
    matn = RichTextField()
    image = models.ImageField(upload_to='Images/qabul_jadvali/', verbose_name="Asosiy Rasm")
    view_count = models.IntegerField(default=0, verbose_name="Ko'rishlar soni")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name_uz and not self.name_en:
            self.name_en = translator.translate(self.name_uz, src='uz', dest='en').text
        if self.name_uz and not self.name_ru:
            self.name_ru = translator.translate(self.name_uz, src='uz', dest='ru').text
        if self.matn_uz and not self.matn_en:
            self.matn_en = translator.translate(self.matn_uz, src='uz', dest='en').text
        if self.matn_uz and not self.matn_ru:
            self.matn_ru = translator.translate(self.matn_uz, src='uz', dest='ru').text
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Qabul Jadvali"
        verbose_name_plural = "Qabul Jadvali"

    
class Murojat(models.Model):
    MUROJAT_TURLARI = [
        ('shikoyat', _('Shikoyat')),
        ('taklif', _('Taklif')),
        ('savol', _('Savol')),
    ]
    
    KIMGA = [
        ('rahbar', _('Rahbar')),
        ('urinbosar', _('O‘rinbosar')),
    ]

    id  = models.AutoField(primary_key=True)
    create_date = models.DateField(auto_now_add=True,verbose_name="Qoyilgan Sana")
    murojat_kimga = models.CharField(max_length=20, choices=KIMGA, default='rahbar')    
    murojat_turi = models.CharField(max_length=20, choices=MUROJAT_TURLARI, default='savol')    
    familiya = models.CharField(max_length=255)
    ismi = models.CharField(max_length=255)
    otasining_ismi = models.CharField(max_length=255,blank=True, null=True)
    kompaniyaning_nomi = models.CharField(max_length=255,blank=True, null=True)
    boglanish_malumotlari = models.CharField(max_length=255)
    pochta_manzil = models.EmailField()
    mirojat_matni = models.TextField()
    hujjatlar = models.FileField(upload_to='murojatlar/',blank=True, null=True) 
    tel_raqam = models.CharField(max_length=20)
    def __str__(self):
        return self.murojat_kimga



class MurojatHammuallif(models.Model):   
    murojat = models.ForeignKey(
        'Murojat',
        related_name="murojat_hammuallif",
        on_delete=models.CASCADE,
        verbose_name="Tegishli Murojat"
    )
    familya = models.CharField(max_length=255)
    ismi = models.CharField(max_length=255)
    otasining_ismi = models.CharField(max_length=255,blank=True, null=True)
    pochta_manzil = models.EmailField()

    def __str__(self):
        return self.familya

