from django.urls import path

from Project1.settings import STATIC_URL
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('Home.html', views.index1, name='index'),
    path('Products.html', views.index1, name='index1'),
    path('Solutions.html', views.index2, name='index2'),
    path('Contacts.html', views.index3, name='index3'),
    path('Enquiry.html', views.index4, name='index4'),
] 

urlpatterns += staticfiles_urlpatterns()