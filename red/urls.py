from django.urls import path
from . import views

app_name = 'red'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('panel/', views.PanelView.as_view(), name='panel'),
    path('post/', views.PostView.as_view(), name='post'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('update_status/', views.update_status, name='update_status'),
]

