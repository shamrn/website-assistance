from django.urls import path
from . import views

urlpatterns = [
    path('assistants/<slug>/', views.WorkerListView.as_view(), name='worker_list'),


    path('add/', views.WorkerCreateView.as_view(), name='worker_add'),


    path('change/<int:pk>/', views.WorkerUpdateView.as_view(), name='worker_change'),

    path('delete/<int:pk>/', views.WorkerDeleteView.as_view(), name='worker_delete'),

    path('search/', views.WorkerSearchView.as_view(), name='search'),

    path('assistants/detail/<slug>/<int:pk>/', views.worker_detail, name='worker_detail'),

    path('take-worker/<slug>/<int:pk>/',views.take_worker,name='take_worker'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),
]