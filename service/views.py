from django.shortcuts import render, redirect
from .models import Category, Subcategory
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from worker.models import City
from .forms import SearchForm


class ServiceListView(ListView):
    model = Category
    template_name = 'service/ServiceList.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city_query'] = City.objects.all()
        context['form_search'] = SearchForm()
        if 'city' not in self.request.session:
            context['city'] = 'не указан'
        else:
            context['city'] = self.request.session['city']
        return context


def city(request, id):
    city = City.objects.get(id=id)
    request.session['city'] = str(city)
    return redirect('service')


class ServiceDetailCategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    extra_context = {'category_': Category.objects.all()}
    template_name = 'service/ServiceDetailCategory.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Category.objects.filter(slug=slug)
