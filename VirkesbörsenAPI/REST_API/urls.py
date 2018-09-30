from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewAll

urlpatterns = {
    url(r'api/$', ViewAll.as_view(), name='getAll')
}

urlpatterns = format_suffix_patterns(urlpatterns)