from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from datetime import datetime
import json

from .models import Paper, DeviceMiLed
from .forms import DeviceStatus


# @require_http_methods(["GET"])
class IndexView(generic.TemplateView):
    template_name = 'red/index.html'


class DetailView(generic.DetailView):
    model = Paper
    template_name = 'red/detail.html'


class PanelView(generic.TemplateView):
    template_name = 'red/panel.html'


class PostView(generic.ListView):
    template_name = 'red/post.html'
    context_object_name = 'latest_paper_list'

    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')[:6]


class ProjectView(generic.TemplateView):
    template_name = 'red/project.html'


@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        form = DeviceStatus(request.POST)
        if form.is_valid():
            return HttpResponse(DeviceMiLed.create(data=request.POST.getlist('data')))
        else:
            return HttpResponse('params are not valid')
    else:
        return HttpResponse(False)
