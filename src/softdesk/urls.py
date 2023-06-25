from django.urls import path, include
from authentication import urls as authentication_urls
from appsoftdesk import urls as appsoftdesk_urls


urlpatterns = [
    path('api/', include(authentication_urls, )),
    path('api/', include(appsoftdesk_urls)),

]
