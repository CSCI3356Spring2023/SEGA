from django.http import HttpResponse

def index(request):
    return HttpResponse("Placeholder for welcome page. \n Please navigate to /admin for the admin panel \n To /summary for a course summary \n And to /createcourse to create a course.")
