from django.urls import path
from . import views


app_name = 'article'

urlpatterns = [
    path(r'', views.FeedsView.as_view(), name='feed'),
    path('<int:pk>', views.DetailView.as_view(), name='details'),
]

