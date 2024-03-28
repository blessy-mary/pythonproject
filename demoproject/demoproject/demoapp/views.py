from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import person
def demo(request):
    obj=place.objects.all()
    return render(request,"index.html",{'result':obj})

def demo(request):
    object=person.objects.all()
    return render(request,"index.html",{'result':object})

