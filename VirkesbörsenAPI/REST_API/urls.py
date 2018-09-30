from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ViewAll, ViewSpecific

urlpatterns = {
    url(r'api/$', ViewAll.as_view(), name='getAll'),
    url(r'api/(?P<pk>[0-9]+)/$', ViewSpecific.as_view(), name='getSpecific')
}

urlpatterns = format_suffix_patterns(urlpatterns)