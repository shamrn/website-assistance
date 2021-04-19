# Generated by Django 3.1.7 on 2021-04-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210412_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('user', 'Пользователь'), ('assistant', 'Ассистент')], default='user', max_length=50, verbose_name='Статус аккаунта'),
        ),
    ]