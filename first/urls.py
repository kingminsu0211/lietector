from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    path('community/', views.community, name='community'),
    path('report/', views.report, name='report'),
    # path('uesr/', include('user.urls')),
]
