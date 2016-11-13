from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello,human. Clark your benevolent overlord has come to solve your emotional menstration.")
def show(request):
    return HttpResponse("You have asked us to show you our penii. We will oblige.")




