from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_views, name="index"),
    path("save/", views.save_index, name='save_input')
]