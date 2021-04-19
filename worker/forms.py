from django import forms
from .models import Worker, City, Country
from service.models import Subcategory, Category
from django.forms.utils import ErrorList
import django_filters


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'birthdate', 'phone', 'country', 'city', 'category', 'subcategory',
                  'body', 'experience', 'price', 'currency', 'caption_price', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by(
                    'name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.country.city_set.order_by('name')


class FilterWorkerForm(django_filters.FilterSet):
    class Meta:
        model = Worker
        fields = ['country', 'city', 'category', 'subcategory']


class FilterWorker(WorkerForm):
    class Meta:
        model = Worker
        fields = ['country', 'city', 'category', 'subcategory']
