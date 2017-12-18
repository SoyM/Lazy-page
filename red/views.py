from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json
import markdown

from .models import Paper, DeviceMiLed, DeviceEspStatus, DeviceEspConfig
from .forms import DeviceStatus, PaperForm, AccountForm


# @require_http_methods(["GET"])
class IndexView(generic.TemplateView):
    template_name = 'red/index.html'


class PostView(generic.ListView):
    template_name = 'red/post.html'
    context_object_name = 'latest_paper_list'

    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')[:6]


class ProjectView(generic.TemplateView):
    template_name = 'red/project.html'


def login(request):
    if request.method == 'POST':
        if AccountForm(request.POST).is_valid:
            user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return render(request, 'red/index.html')
            else:
                return render(request, 'red/login.html')
        else:
            return render(request, 'red/login.html')
    else:
        if request.user.is_authenticated:
            HttpResponseRedirect('/')
        return render(request, 'red/login.html', {
            'uf': AccountForm,
        })


def paper_detail(request, pk):
    paper = get_object_or_404(Paper, pk=pk)
    return render(request, 'red/detail.html', {
        'id': paper.id,
        'title': paper.title,
        'pub_date': paper.pub_date,
        'content': markdown.markdown(paper.content),
    })


def paper_edit(request, pk):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            Paper.edit(pk, request.POST['title'], request.POST['content'])
            return HttpResponseRedirect('/%d/' % pk)
        else:
            return HttpResponse('params is not valid')
    else:
        paper = get_object_or_404(Paper, pk=pk)
        return render(request, 'red/paper_edit.html', {
            'id': paper.id,
            'title': paper.title,
            'pub_date': paper.pub_date,
            'content': paper.content.replace('\r\n', '\\r\\n'),
        })


@login_required()
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
