from django.conf.urls import url

from .views import LogParsingFormView


urlpatterns = [
    url(r'^parse/$', LogParsingFormView.as_view(), name="parse"),
]
