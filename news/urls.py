from django.urls import path
from news.views import *
urlpatterns = [
    path('', home),
    path('news1/', home),
    path('news2/', home),
    path('news3/', home),
    path('news4/', home),
]