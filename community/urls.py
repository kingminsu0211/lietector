from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    #게시글
    path('posts/search/', PostSearchAPIView.as_view(), name='post-search'),
    path('posts/mylist/', MyPostListView.as_view(), name='mypost_list'),
    path('posts/alllist/', AllPostListView.as_view(), name='allpost_list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/', create_post, name='create_post'),
    path('posts/update/<int:post_id>/', update_post, name='update_post'),
    #댓글
    path('posts/<int:post_id>/comment/', comment_write, name='comment-write'),
    path('posts/comment/update/<int:comment_id>/', comment_update, name='comment_update'),
    path('posts/comment/mycomment/', MyCommentListView.as_view(), name='my-comment'),
    path('posts/comment/allcomment/', AllCommentListView.as_view(), name='all-comment'),
    #신고하기
    path('reports/', report, name='reports'),
    path('reports/<int:report_id>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/update/<int:report_id>/', report_update, name='report_update'),
    path('reports/myreport/', MyReportListView.as_view(), name='myreport_list'),
    path('reports/allreport/', AllReportListView.as_view(), name='allreport_list'),
    #문의하기
    path('ask/', create_ask, name='create_ask'),
    path('ask/update/<int:post_id>/', update_ask, name='update_ask'),
    path('ask/<int:post_id>/comment/', ask_comment_write, name='ask_comment'),
    # 다른 URL 패턴들을 필요에 따라 추가
]
