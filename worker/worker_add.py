from .models import Worker, Country, City
from account.models import CustomUser
from service.models import Category, Subcategory
import random
import os
from django.core.files import File


def add():
    for _ in range(1000):
        user = CustomUser.objects.get(username='vlad')
        data = '{y}-{m}-{d}'.format(d=random.randint(1, 28), m=random.randint(1, 12), y=random.randint(1950, 2000))
        with open('../assistance/load-data/name/rus-man.txt', 'r') as f:
            name_man = f.read().split('\n')
        with open('../assistance/load-data/name/run-woman.txt', 'r') as f:
            name_woman = f.read().split('\n')
        rand_name = random.randint(1, 2)
        country = Country.objects.order_by('?').first()
        city = City.objects.filter(country=country).order_by('?').first()
        category = Category.objects.order_by('?').first()
        subcategory = Subcategory.objects.filter(category_id=category).order_by('?').first()
        phone = ''.join(random.choices(('7918420212', '79284101221', '74951126816', '75151281521', '79995125921')))
        experience = random.randint(int(data[0:4]) + 18, 2020)
        body = 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. '
        price = random.randint(500, 5000)
        if str(country.name) == 'Россия':
            currency = 'руб'
        elif str(country.name) == 'Казахстан':
            currency = 'тенге'
        else:
            currency = 'грн'
        caption_price = ''.join(random.choices(('услуга', 'по договорённости', '60 минут')))
        if (rand_name == 1 or str(category.name) == 'Косметология') and str(category.name) != 'Ремонт':
            name = ''.join(random.choices(name_woman))
            photo_path = '../assistance/load-data/img/' + ''.join(
                random.choices(('woman-1.jpg', 'woman-2.jpg', 'woman-3.jpg',
                                'woman-4.jpg', 'woman-5.jpg', 'woman-6.jpg'
                                )))
        else:
            name = ''.join(random.choices(name_man))
            photo_path = '../assistance/load-data/img/' + ''.join(random.choices(('man-1.jpg', 'man-2.jpg', 'man-3.jpg',
                                                                                  'man-4.jpg', 'man-5.jpg', 'man-6.jpg',
                                                                                  'man-7.jpg', 'man-8.jpg')))
        photo = File(open(photo_path, 'rb'))

        Worker.objects.create(user=user, name=name, birthdate=data, country=country, city=city, category=category,
                              subcategory=subcategory, phone=phone, experience=experience, body=body, price=price,
                              currency=currency, caption_price=caption_price, photo=photo)
        print('Запись')
