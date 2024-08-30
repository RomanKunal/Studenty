from django.shortcuts import render

# Create your views here.
from . models import Student


def home(request):
    show=Student.objects.all()
    return render(request,'home.html',{'show':show})

def fetch(request):
    data = Student.objects.filter(Sname__endswith='t')  
    return render(request, 'fetch.html', {'data': data})
    
