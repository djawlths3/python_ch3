from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'helloworld/hello.html')

def hello2(request, id=0):
    return render(request, 'helloworld/hello.html')

def hello3(request, id=0):
    jsonresult = {
        'result' : 'success',
        'data' : ['hello', 1, 2, True, ('a','b','c')]
    }
    return JsonResponse(jsonresult)