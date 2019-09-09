from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from crawler.views import Crawl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-token/', obtain_auth_token, name='auth_token'),
    path('result/', Crawl.as_view(), name='result'),
]
