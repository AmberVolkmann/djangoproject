from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def is how we create a function/method in python
def index(request):
    # return HttpResponse('Hello from post!')

    return render(request, 'posts/index.html')
