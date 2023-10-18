import pytest

from django.http import HttpRequest, HttpResponse
from django.test import Client
from django.urls import path

from django_di import context, view

class Service:
    pass


urlpatterns = []


@pytest.mark.urls(__name__)  # See: https://adamj.eu/tech/2020/10/15/a-single-file-rest-api-in-django/
def test_view_di_decorator():
    test_client = Client()

    context.DI.register_singleton(Service, Service())
    
    @view.di
    def index(_: HttpRequest, service: Service):
        assert service is not None, "service was not injected"
        return HttpResponse()

    global urlpatterns   
    urlpatterns = [path("", index)]
    
    test_client.get("")    
