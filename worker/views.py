from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Worker, Country, City
from .forms import WorkerForm, FilterWorkerForm, FilterWorker
from service.models import Category, Subcategory
from account.models import CustomUser
from django_filters.views import FilterView
from django.contrib import messages


class WorkerListView(FormMixin, FilterView):
    model = Worker
    paginate_by = 6
    form_class = FilterWorker
    context_object_name = 'worker'
    template_name = 'worker/worker_list.html'
    filterset_class = FilterWorkerForm

    def get_queryset(self):
        if self.request.GET:
            if 'subcategory' in self.request.GET:
                return Worker.objects.all()
        else:
            slug = self.kwargs['slug']
            if 'city' in self.request.session:
                return Worker.objects.filter(subcategory__slug=slug, city__name=self.request.session['city'])
            else:
                return Worker.objects.filter(subcategory__slug=slug)


class WorkerSearchView(WorkerListView):
    def get_queryset(self):
        super().get_queryset()
        if 'query' in self.request.GET:
            query = self.request.GET['query']
            search_vector = SearchVector('name', 'subcategory', 'category', 'body')
            search_query = SearchQuery(query)
            results = Worker.objects.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)). \
                filter(search=search_query)
            return results


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'worker/city_dropdown_list_options.html', {'cities': cities})


def load_subcategory(request):
    category_id = request.GET.get('category')
    subcategory = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request, 'worker/subcategory_dropdown_list_options.html', {'subcategory': subcategory})


class WorkerCreateView(CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = 'worker/worker_create.html'
    success_url = reverse_lazy('dashboard')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerCreateView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        user = CustomUser.objects.get(username=instance.user)
        user.status = 'assistant'
        user.save()
        return super(WorkerCreateView, self).form_valid(form)


class WorkerUpdateView(UpdateView):
    model = Worker
    fields = ('name', 'birthdate', 'phone', 'country', 'city', 'category', 'subcategory', 'body',
              'experience', 'price', 'currency', 'caption_price', 'photo'
              )
    template_name = 'worker/worker_update.html'
    success_url = reverse_lazy('dashboard')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerUpdateView, self).dispatch(request, *args, **kwargs)


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'worker/worker_delete.html'
    context_object_name = 'worker'
    success_url = reverse_lazy('dashboard')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(WorkerDeleteView, self).dispatch(request, *args, **kwargs)


def worker_detail(request, slug, pk):
    worker = Worker.objects.get(id=pk)
    return render(request, 'worker/worker_detail.html', {'worker': worker})


def take_worker(request, slug, pk):
    worker = Worker.objects.get(pk=pk)
    phone = worker.phone
    name = worker.name.split()[1]
    if request.user.is_authenticated:
        return render(request, 'worker/take_worker.html', {'name': name, 'phone': phone})
    else:
        request.session['redirect_login'] = [worker.get_absolute_url()]
        messages.success(request, 'Для продолжения войдите в свой аккаунт')
        return redirect('login')
