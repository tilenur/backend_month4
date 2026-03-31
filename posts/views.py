from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
  return HttpResponse("Hello Django!")

def main(request):
  return render(request, "base.html")

def about(request):
  return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")
