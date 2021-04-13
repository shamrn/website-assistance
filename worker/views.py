from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView
from .models import Worker,Country,City
from .forms import WorkerForm
from service.models import Category,Subcategory

class WorkerListView(ListView):
    model = Worker
    context_object_name = 'worker'
    template_name = 'worker/worker_create.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerListView, self).dispatch(request, *args, **kwargs)


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request,'worker/city_dropdown_list_options.html',{'cities':cities})

def load_subcategory(request):
    category_id = request.GET.get('category')
    subcategory = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request,'worker/subcategory_dropdown_list_options.html',{'subcategory':subcategory})


class WorkerCreateView(CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = 'worker/worker_create.html'
    success_url = reverse_lazy('worker_changelist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super(WorkerCreateView, self).form_valid(form)



class WorkerUpdateView(UpdateView):
    model = Worker
    fields = ('name','birthdate','phone','country','city','category','subcategory','body')
    template_name = 'worker/worker_create.html'
    success_url = reverse_lazy('worker_changelist')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerUpdateView, self).dispatch(request, *args, **kwargs)