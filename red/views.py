from django.views import generic
from .models import Paper, DeviceMiLed
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


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


def update_status(request):
    if request.method == 'GET':
        return HttpResponse(False)
    if request.method == 'POST':
        form = DeviceMiLed(request.POST)
        if form.is_valid():
            return HttpResponse("Hello, world. You're at the polls index.")