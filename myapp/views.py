from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
   return render(request, 'myapp/Home.html')

def index1(request): 
   return render(request, 'myapp/Products.html')

def index2(request): 
   return render(request, 'myapp/Solutions.html')

def index3(request): 
   return render(request, 'myapp/Contacts.html')

def index4(request): 
   return render(request, 'myapp/Enquiry.html')