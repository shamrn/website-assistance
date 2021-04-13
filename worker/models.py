from django.db import models
from account.models import CustomUser
from service.models import Category,Subcategory


class Country(models.Model):
    name = models.CharField(max_length=50,verbose_name='Страна')

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, related_name='city',on_delete=models.CASCADE,verbose_name='Страна')
    name = models.CharField(max_length=50,verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

class Worker(models.Model):

    STATUS_CHOICES = (
        ('active','Анкета активна'),
        ('no-active','Анкета не активна')
    )

    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name='Пользователь')
    name = models.CharField(max_length=100,verbose_name='Фио')
    birthdate = models.DateField(verbose_name='Дата рождения')
    country = models.ForeignKey(Country,null=True,on_delete=models.SET_NULL,verbose_name='Страна')
    city = models.ForeignKey(City,null=True,on_delete=models.SET_NULL,verbose_name='Город')
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL,verbose_name='Категория услуги')
    subcategory = models.ForeignKey(Subcategory,null=True,on_delete=models.SET_NULL,verbose_name='Подкатегория услуги')
    phone = models.CharField(max_length=100,verbose_name='Номер телефона')
    body = models.TextField(verbose_name='О себе')

    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='no-active',verbose_name='Статус')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name