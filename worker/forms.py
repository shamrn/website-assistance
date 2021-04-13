from django import forms
from .models import Worker,City
from service.models import Subcategory,Category

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ['name','birthdate','phone','country','city','category','subcategory','body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.country.city_set.order_by('name')