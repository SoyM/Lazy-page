from django.urls import path
from red import views

app_name = 'red'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('project/', views.ProjectView.as_view(), name='project'),
    # auth
    path('login/', views.login, name='login'),
    # post
    path('p/<str:title>/', views.paper_detail, name='detail'),
    path('p/', views.post, name='post'),
    # panel
    path('panel/', views.panel, name='panel'),
    path('panel_data/', views.panel_data, name='panel_data'),
    path('update_status/', views.update_status, name='update_status'),
    path('get_set_motion/', views.get_set_motion, name='get_set_motion'),
    path('get_bot_motion/', views.get_bot_motion, name='get_bot_motion'),
    path('change_bot_motion', views.change_bot_motion, name='change_bot_motion'),
    path('update_bot_motion/', views.update_bot_motion, name='update_bot_motion'),
]
