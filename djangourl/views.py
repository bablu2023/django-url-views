#django http response
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django home page!")

def aboutUs(request):
    return HttpResponse("This is the about us page.")
def course(request):
    return HttpResponse("This is the course page.")
def courseDetails(request, courseid):
    return HttpResponse(f"This is the details of course with id: {courseid}")
#make dynamic url for course details page with courseid as parameter
#example url: /course/101
#example url: /course/202
#example url: /course/303
#example url: /course/404
#example url: /course/505

#str url parameter
#example url: /course/python
#example url: /course/django
#example url: /course/javascript
#example url: /course/reactjs
#example url: /course/angular

def courseDetailsStr(request, coursename):
    return HttpResponse(f"This is the details of course with name: {coursename}")
# slug url parameter
#example url: /course/python-for-beginners
#example url: /course/django-for-beginners
#example url: /course/javascript-for-beginners
#example url: /course/reactjs-for-beginners

def courseDetailsSlug(request, courseslug):
    return HttpResponse(f"This is the details of course with slug: {courseslug}")
#example url: /course/python-for-beginners
