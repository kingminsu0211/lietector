from django.views.generic import ListView, DetailView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        # Assuming the serializer has 'title' and 'content' fields
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        report_number = serializer.validated_data.get('report_number')

        # You can access the authenticated user using request.user
        user = request.user

        # Create a new Post object
        post =Post.objects.create(title=title, content=content, writer=user, report_number=report_number)

        return Response({'message': '게시물이 성공적으로 작성되었습니다.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['POST'])
# def create_post(request):
#     # 현재 로그인한 사용자 정보 가져오기
#     user = request.user
#
#     # POST 데이터에 로그인한 사용자 정보 추가
#     data = request.data.copy()
#     data['writer'] = user.id
#
#     serializer = PostSerializer(data=data, context={'user': user})
#
#     if serializer.is_valid():
#         # serializer에서 로그인한 사용자 정보를 가져와서 Post 객체 생성
#         post = serializer.save()
#
#         return Response({'message': '게시물이 성공적으로 작성되었습니다.'}, status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
