from django.urls import path
from .views import HomeView, SignUp, gitsync, get_status
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignUp.as_view(), name='signup'),
    path('gitsync', gitsync, name='gitsync'),
    path('task/<sync_id>/<task_id>', get_status, name='gitsync')
]