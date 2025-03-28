from django.db import models

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
        verbose_name = "Matbuot Xizmati Rasmi"
        verbose_name_plural = "Matbuot Xizmati Rasmlari"


class MatbuotXizmati(models.Model):
    title = models.CharField(max_length=455, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='matbuot/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Matbuot Xizmati"
        verbose_name_plural = "Matbuot Xizmati"
        ordering = ['-id']


# Models for Elon va Tadbirlar
class ElonVaTadbirlarRasmlar(models.Model):
    image = models.ImageField(upload_to="elon_va_tadbirlar/", verbose_name="Elon va Tadbir Rasmi")
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
    image = models.ImageField(upload_to='elon_va_tadbirlar/', verbose_name="Asosiy Rasm")
    content = models.TextField(verbose_name="Kontent")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan Sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan Sana")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Elon va Tadbir"
        verbose_name_plural = "Elon va Tadbirlar"
        ordering = ['-id']
