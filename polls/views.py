from django.http import HttpResponse


def index(request):
    return HttpResponse("Pipeline POC using Render - Test Redis preview env")
