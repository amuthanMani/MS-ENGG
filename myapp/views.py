from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_screen_view(request):
   print(request.headers)
   return render(request, "Base.html", {})

def index(request): 
   return render(request, 'Home.html')

def index1(request): 
   return render(request, 'Products.html')

def index2(request): 
   return render(request, 'Solutions.html')

def index3(request): 
   return render(request, 'Contacts.html')

def index4(request): 
   return render(request, 'Enquiry.html')