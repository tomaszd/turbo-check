# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Monitor! says hello world!")