from django.http import HttpResponse
def foo(request):
    return HttpResponse ("hello there!")