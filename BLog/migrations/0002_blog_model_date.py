# Generated by Django 3.1.4 on 2021-01-03 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BLog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_model',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
