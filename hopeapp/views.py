
from django.shortcuts import render,redirect
from hopeapp.models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def details(request):
    return render(request,'blog-details.html')

def blog(request):
    return render(request,'blog.html')
def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def testmonials(request):
    return render(request,'testimonials.html')
def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')


def login_view(request):
    return render(request, 'login.html')



