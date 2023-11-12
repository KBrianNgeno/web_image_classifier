from django.urls import path
# from django.utils.http import urlsafe_base64_decode

from .views import classify

# imgdata = urlsafe_base64_decode(imgstring)
# base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'


urlpatterns = [
    path('img/<str:imgstring>', classify, name='classify'),
    # path(r'^img/(?P<imgstring>{})/'.format(base64_pattern), classify, name='classify'),
]
