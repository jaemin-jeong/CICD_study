from django.http import HttpResponse


def index(request):
    return HttpResponse(">> user root page")
