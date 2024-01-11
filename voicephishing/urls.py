from django.urls import include, path
from .views import VoicePhishingRecordListView, VoicePhishingRecordDetailView
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('user/', include('user.urls')),
    path('community/', include('community.urls')),
    path('records/', VoicePhishingRecordListView.as_view(), name='record-list'),
    path('records/<int:pk>/', VoicePhishingRecordDetailView.as_view(), name='record-detail'),
    # 다른 URL 패턴들을 필요에 따라 추가
]
