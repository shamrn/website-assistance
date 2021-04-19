from django.urls import path
from . import views

urlpatterns = [
    path('',views.ServiceListView.as_view(),name='service'),
    path('city/<int:id>/',views.city,name='city'),
    path('category/<slug>/',views.ServiceDetailCategoryView.as_view(),name='service_detail'),


]