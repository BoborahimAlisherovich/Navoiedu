from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

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
    updated_at = models.DateTimeField(auto_now=True, verbose_name=" ilangan Sana")

    def __str__(self):
        return self.title

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangiliklar "
        verbose_name_plural = "Yangiliklar "
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
    title = models.CharField(max_length=455, verbose_name="Sarlavha",)
    image = models.ImageField(upload_to='Images/elon_va_tadbirlar/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Elon va Tadbir"
        verbose_name_plural = "Elon va Tadbirlar"
        ordering = ['-id']




#new addit
class BoShIshOrin(models.Model):
    image = models.ImageField(upload_to='Images/bo_shish_orin/', verbose_name="Rasm")
    lavozim = models.CharField(max_length=100)
    joylashuv = models.CharField(max_length=100)
    sana = models.DateField()
    tavsif = models.TextField()
    boshqarma_tarix = models.ForeignKey(
        'BoshqarmaTarixi',
        related_name="BoShIshOrin",
        on_delete=models.CASCADE,
        verbose_name="Tegishli boshqarma tarix"
    )

    def __str__(self):
        return self.lavozim
    

class Rahbariyat(models.Model):
    ism = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/rahbariyat/',verbose_name="Rasm")
    lavozim = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()
    boshqarma_tarix = models.ForeignKey(
        'BoshqarmaTarixi',
        related_name="Rahbariyatlar",
        on_delete=models.CASCADE,
        verbose_name="Tegishli Rahbariyat"
    )

    def __str__(self):
        
        
        return self.ism

class BoshqarmaTarixi(models.Model):
    image = models.ImageField(upload_to='Images/boshqarma_haqida/', verbose_name="Asosiy Rasm")
    title = models.CharField(max_length=255,verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Boshqarma Haqida"
        verbose_name_plural = "Boshqarma Haqida"


# class BoshqarmaTarixi(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    

    
# class TarkibiyTuzilma(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
#     boshqarma_tarix = models.ForeignKey(
#         'BoshqarmaTarixi',
#         related_name="TarkibiyTuzilma",
#         on_delete=models.CASCADE,
#         verbose_name="Tegishli TarkibiyTuzilma"
#     )


    
class QabulJadvali(models.Model):
    name = models.CharField(max_length=255, verbose_name="Politexnikum nomi")
    matn = RichTextField()
    image = models.ImageField(upload_to='Images/qabul_jadvali/', verbose_name="Asosiy Rasm")
    # boshqarma_tarix = models.ForeignKey(
    #     'BoshqarmaTarixi',
    #     related_name="QabulJadvali",
    #     on_delete=models.CASCADE,
    #     verbose_name="Tegishli QabulJadvali"
    # )

    def __str__(self):
        return self.name





    
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

