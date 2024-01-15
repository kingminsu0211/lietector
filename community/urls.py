from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(r'postcheck', PostViewset)
# router.register(r'commentcheck', CommentViewset)
# router.register(r'reportcheck', ReportViewset)

urlpatterns = [
    path('posts/', create_post, name='create_post'),
    path('posts/update/<int:post_id>/', update_post, name='update_post'),
    path('comment/', CommentListView().as_view(), name='comment_list'),
    path('comments/<int:post_id>/', comment_write, name='comment-write'),
    path('comments/update/<int:comment_id>/', comment_update, name='comment_update'),
    path('reports/', report, name='reports'),

    # 다른 URL 패턴들을 필요에 따라 추가
]
