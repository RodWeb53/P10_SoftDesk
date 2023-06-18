from django.urls import path, include
from authentication import urls as authentication_urls


urlpatterns = [
    path('api/', include(authentication_urls)),

]
