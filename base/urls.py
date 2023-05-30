from django.urls import path
from . import views


# Follow the pattern exactly

urlpatterns = [
    path('', views.home, name = "home"),
    path('poems/', views.first_post, name = "poems"),
    path('stories/', views.second_post, name = "stories"),
    path('third_post/', views.third_post, name = "third-post")
]