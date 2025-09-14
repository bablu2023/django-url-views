#django http response
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django home page!")

def aboutUs(request):
    return HttpResponse("This is the about us page.")
