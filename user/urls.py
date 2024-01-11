from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()

router.register(r'check', views.CheckAccountViewset)


urlpatterns = [
    path('',include(router.urls)),
    path('first/', include('first.urls')),
    path('signup/', signup, name='signup'),
    # path('register/', register, name='register'),
]