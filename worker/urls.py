from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkerListView.as_view(), name='worker_changelist'),
    path('add/', views.WorkerCreateView.as_view(), name='worker_add'),
    path('<int:pk>/', views.WorkerUpdateView.as_view(), name='worker_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-subcategory/', views.load_subcategory, name='ajax_load_subcategory'),
]