from django.http import HttpResponse
from django.template import loader
from .models import Course

def registercourse(request):
    mycourses = Course.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mycourses': mycourses,
    }
    return HttpResponse(template.render(context, request))
