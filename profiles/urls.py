from django.urls import path

from profiles.views.hello import hello_view

urlpatterns = [
    path("hello/", hello_view),
]
