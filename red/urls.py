from django.urls import path
from red import views

app_name = 'red'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.paper_detail, name='detail'),
    path('panel/', views.panel, name='panel'),
    path('post/', views.PostView.as_view(), name='post'),
    path('project/', views.ProjectView.as_view(), name='project'),
    path('update_status/', views.update_status, name='update_status'),
    path('<int:pk>/paper_edit/', views.paper_edit, name='paper_edit')
]
