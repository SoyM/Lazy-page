from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Paper


class IndexView(generic.ListView):
    template_name = 'red/index.html'
    context_object_name = 'latest_paper_list'

    def get_queryset(self):
        return Paper.objects.order_by('-pub_date')[:6]


class DetailView(generic.DetailView):
    model = Paper
    template_name = 'red/detail.html'


class PanelView(generic.ListView):
    model = Paper
    template_name = 'red/panel.html'


class PostView(generic.ListView):
    model = Paper
    template_name = 'red/post.html'


class ProjectView(generic.ListView):
    model = Paper
    template_name = 'red/project.html'
