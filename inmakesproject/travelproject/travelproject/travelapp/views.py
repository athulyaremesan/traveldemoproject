from django.shortcuts import render
from django .http import HttpResponse
# Create your views here.
from .models import Place, Team


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()

    return  render(request,'index.html',{'result':obj,'result1':obj1})
