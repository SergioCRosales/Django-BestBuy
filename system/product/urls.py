from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.begin, name='begin'),
    path('about', views.about, name='about'),
    path('products', views.products, name='products'),
    path('products/create', views.create, name='create'),
    path('products/edit', views.edit,name='edit'),
    path('eliminate/<int:id>', views.eliminate, name='eliminate'),
    path('products/edit/<int:id>', views.edit,name='edit'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)