# Generated by Django 3.1.7 on 2021-04-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20210414_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/worker/', verbose_name='Изображение'),
        ),
    ]