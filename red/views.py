from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import os
import json
import markdown
from .mqttController import MqttController
from .models import DeviceMiLed, MachineParams, BotMotion
from .forms import AccountForm, MachineParamsForm

mqtt = MqttController()


# @require_http_methods(["GET"])
class IndexView(generic.TemplateView):
    template_name = 'red/index.html'


def post(request):
    file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'paper'
    paper = {}
    for root, dirs, files in os.walk(file_dir):
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
        count = 0
        for paper_title in files:
            paper[count] = paper_title[:-3]
            count += 1
    return render(request, 'red/post.html', {
        'paper': paper,
    })


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
                return HttpResponseRedirect('/login/')
        else:
            return render(request, 'red/login.html')
    else:
        if request.user.is_authenticated:
            HttpResponseRedirect('/')
        return render(request, 'red/login.html', {
            'uf': AccountForm,
        })


def paper_detail(request, title):
    file_object = open(
        os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'paper' + os.path.sep + title + '.md')
    try:
        content = file_object.read()
    finally:
        file_object.close()

    return render(request, 'red/detail.html', {
        'title': title,
        'content': markdown.markdown(content),
    })


def panel_data(request):
    esp_list = get_list_or_404(MachineParams)
    params = get_object_or_404(MachineParams, pk=esp_list[len(esp_list) - 1].id)
    return HttpResponse(
        json.dumps({
            # 'power': miled_data['power'],
            # 'bright': miled_data['bright'],
            'temperature': params.temperature,
            'humidity': params.humidity,
            'mq': params.mq,
            'ap_ssid': params.ssid,
        })
    )


@login_required()
def panel(request):
    esp_list = get_list_or_404(MachineParams)
    esp_data = get_object_or_404(MachineParams, pk=esp_list[len(esp_list) - 1].id)
    return render(request, 'red/panel.html', {
        'temperature': esp_data.temperature,
        'humidity': esp_data.humidity,
        'mq': esp_data.mq,
        'ap_ssid': esp_data.ssid,
    })


@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.read().decode('utf-8'))
        form = MachineParamsForm(data)
        if form.is_valid():
            return HttpResponse(MachineParams.create(data))
        else:
            return HttpResponse('params are not valid')
    else:
        return HttpResponse(False)


@csrf_exempt
def get_set_motion(request):
    try:
        response_data = BotMotion.objects.get(pk=1)
    except:
        return HttpResponse(False)

    return HttpResponse(json.dumps({
        'set_mode': response_data.set_mode,
        'update_date': response_data.update_date.timestamp(),
    }))


@csrf_exempt
def get_bot_motion(request):
    try:
        response_data = BotMotion.objects.get(pk=1)
    except:
        return HttpResponse(False)

    return HttpResponse(json.dumps({
        'bot_mode': response_data.bot_mode,
        'update_date': response_data.update_date.timestamp(),
    }))


@csrf_exempt
def change_bot_motion(request):
    set_mode = request.GET['set_mode']
    mqtt.client.publish("set_mode", json.dumps({"set_mode": set_mode}))
    data = {'set_mode': set_mode}
    return HttpResponse(BotMotion.create(data))


@csrf_exempt
def update_bot_motion(request):
    if request.method == 'POST':
        data = json.loads(request.read().decode('utf-8'))
        return HttpResponse(BotMotion.create(data))
