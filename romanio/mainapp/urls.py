from django.contrib import admin
from django.urls import path
from django.conf import settings 

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('catalog/<str:slug_url>/',CatalogPage.as_view(), name="category"),
    path('catalog/<str:slug_category>/<str:slug_url>/', ProductDetail.as_view(), name="product_detail"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('complete_reg/',PhoneAddView.as_view(),{'next_page': settings.LOGIN_REDIRECT_URL}, name='phone_add' ),
    path('contact/',ContactPage.as_view(), name='contact' ),
    path('catalog/<str:slug_subcategory>/', SubCategoryView.as_view(), name='subcategory')    
]