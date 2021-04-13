from django.db import models

class Category(models.Model):

    STATUS_CHOICES = (
        ('active','Категория активна'),
        ('not-active','Не активна'),
    )

    name = models.CharField(max_length=100,verbose_name='Название')
    slug = models.SlugField(max_length=100,unique=True)
    photo = models.ImageField(upload_to=f'photos/',verbose_name='Изображение')
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,verbose_name='Статус')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Subcategory(models.Model):

    STATUS_CHOICES = (
        ('active','Категория активна'),
        ('not-active','Не активна'),
    )

    category_id = models.ForeignKey(Category,related_name='subcategory',on_delete=models.CASCADE,verbose_name='Подкатегория')
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, verbose_name='Статус')


    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name