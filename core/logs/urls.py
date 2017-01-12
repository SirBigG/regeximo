from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import LogParsingFormView, SearchView


urlpatterns = [
    url(r'^parse/$', LogParsingFormView.as_view(), name="parse"),
    url(r'^search/$', csrf_exempt(SearchView.as_view()), name="search"),
]
