# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = "uploader"

urlpatterns = [
    re_path(r"^upload/$", csrf_exempt(views.FineUploaderView.as_view()), name="upload"),
]
