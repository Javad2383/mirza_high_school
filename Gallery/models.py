from django.db import models
from image_optimizer.fields import OptimizedImageField


def upload_image(instance, filename):
    return f"Gallery/{instance}/{filename}"


class Gallery_Main(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان تصاویر")
    image_title = OptimizedImageField(
        upload_to=upload_image,
        verbose_name="عکس نمایشی",
        optimized_image_resize_method='cover',
        optimized_image_output_size=(300, 300),
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"


class Gallery_Detail(models.Model):
    image_alt = models.SlugField(verbose_name="نام عکس")
    image = OptimizedImageField(
        upload_to=upload_image,
        verbose_name="عکس",
        optimized_image_resize_method='cover',
        optimized_image_output_size=(350, 350),
    )
    image_group = models.ForeignKey(Gallery_Main, on_delete=models.CASCADE, verbose_name="افزودن به : ")

    def __str__(self):
        return self.image_alt

    class Meta:
        verbose_name = "جزییات گالری"
        verbose_name_plural = "جزییات گالری"
