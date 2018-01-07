from django.urls import path
from red import views

app_name = 'red'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/', views.ProjectView.as_view(), name='project'),
    # auth
    path('login/', views.login, name='login'),
    # post
    path('p/<str:title>', views.paper_detail, name='detail'),
    path('p/', views.post, name='post'),
    # panel
    path('panel/', views.panel, name='panel'),
    path('update_status/', views.update_status, name='update_status'),
]
