from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django_q.tasks import async_task, result


def index(request):
    template = loader.get_template('index.html')
    async_task('math.copysign', 2, -2)

    return HttpResponse(template.render())

def task(request):
    context_instance = RequestContext(request)
    return HttpResponse("Task")