from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import static
from Project1.settings import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('Products.html', views.index1, name='index1'),
    path('Solutions.html', views.index2, name='index2'),
    path('Contacts.html', views.index3, name='index3'),
    path('Enquiry.html', views.index4, name='index4'),

] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)