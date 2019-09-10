from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from crawler.views import Crawl
from demo.views import Index, DemoCrawl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth-token/', obtain_auth_token, name='auth_token'),
    path('result/', Crawl.as_view(), name='result'),

    path('', Index.as_view(), name='index'),
    path('demo-crawl/', DemoCrawl.as_view(), name='crawl'),
]
