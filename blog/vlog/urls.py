from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help_list, name='help_list'),
    path('help/<int:pk>/', views.help_detail, name='help_detail'),
    path('help/item/<int:item_pk>/', views.help_item_detail, name='help_item_detail'),
    path('search/', views.search, name='search'),
    path('vent/<int:pk>/', views.vent_detail, name='vent_detail'),
    path('vent/', views.vent, name='vent'),
    path('vent_success/', views.vent_success, name='vent_success'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:slug>/', views.category, name='category_detail'),

  
]