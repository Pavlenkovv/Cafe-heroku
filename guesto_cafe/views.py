from django.http import HttpResponse

def hello(request):
    print(request)
    print(dir(request))
    return HttpResponse('<h1>Hello, World!</h1>')
