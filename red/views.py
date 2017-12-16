from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from datetime import datetime
import json

from .models import Paper, DeviceMiLed, DeviceEspStatus, DeviceEspConfig
from .forms import DeviceStatus, PaperForm


# @require_http_methods(["GET"])
class IndexView(generic.TemplateView):
    template_name = 'red/index.html'


class DetailView(generic.DetailView):
    model = Paper
    template_name = 'red/detail.html'


class PostView(generic.ListView):
    template_name = 'red/post.html'
    context_object_name = 'latest_paper_list'

    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')[:6]


class ProjectView(generic.TemplateView):
    template_name = 'red/project.html'


def paper_edit(request, pk):
    if (request.method == 'POST'):
        form = PaperForm(request.POST)
        if form.is_valid():
            return HttpResponse(Paper.create(request.POST['title'], request.POST['content']))
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'red/paper_edit.html', {
        'id': paper.id,
        'title': paper.title,
        'content': paper.content,
    })


def panel(request):
    miled_list = get_list_or_404(DeviceMiLed)
    miled_data = json.loads(get_object_or_404(DeviceMiLed, pk=miled_list[len(miled_list) - 1].id).data)
    esp_list = get_list_or_404(DeviceEspStatus)
    esp_data = get_object_or_404(DeviceEspStatus, pk=esp_list[len(esp_list) - 1].id)

    return render(request, 'red/panel.html', {
        'power': miled_data['power'],
        'bright': miled_data['bright'],
        'temperature': esp_data.temperature,
        'humidity': esp_data.humidity,
        'mq': esp_data.mq,
        'ap_ssid': esp_data.ssid,
    })


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
