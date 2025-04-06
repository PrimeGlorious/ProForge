from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. This is the index page.")
