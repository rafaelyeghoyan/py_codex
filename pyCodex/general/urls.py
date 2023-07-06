from django.urls import path
from . import views
urlpatterns = [
    path('', views.general.as_view()),

]