# Generated by Django 3.1.4 on 2021-01-03 10:09

import Gallery.models
from django.db import migrations, models
import django.db.models.deletion
import image_optimizer.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان تصاویر')),
                ('image_title', image_optimizer.fields.OptimizedImageField(upload_to=Gallery.models.upload_image, verbose_name='عکس نمایشی')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.CreateModel(
            name='Gallery_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_alt', models.SlugField(verbose_name='نام عکس')),
                ('image', image_optimizer.fields.OptimizedImageField(upload_to=Gallery.models.upload_image, verbose_name='عکس')),
                ('image_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gallery.gallery_main', verbose_name='افزودن به : ')),
            ],
            options={
                'verbose_name': 'جزییات گالری',
                'verbose_name_plural': 'جزییات گالری',
            },
        ),
    ]
