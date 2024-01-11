from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(r'postcheck', PostViewset)
# router.register(r'commentcheck', CommentViewset)
# router.register(r'reportcheck', ReportViewset)

urlpatterns = [
    path('posts/', create_post, name='craete_post'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('reports/', ReportListView.as_view(), name='report-list'),
    # 다른 URL 패턴들을 필요에 따라 추가
]
