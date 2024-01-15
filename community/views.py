from django.views.generic import ListView, DetailView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReportListView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


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

@api_view(['PUT'])  # 또는 ['PATCH']를 사용할 수 있습니다.
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.writer:
        return Response({'error': '게시물을 수정할 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = PostSerializer(post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': '게시물이 성공적으로 수정되었습니다.'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def comment_write(request, post_id):
    serializer = CommentSerializer(data=request.data)

    if serializer.is_valid():
        content = serializer.validated_data.get('content')
        user_id = serializer.validated_data.get('user')
        post_id = serializer.validated_data.get('post')

        # 사용자 및 게시물 인스턴스를 가져옵니다
        user = get_object_or_404(CustomUser, id=user_id.id)
        post = get_object_or_404(Post, id=post_id.id)

        # 새로운 댓글 객체를 생성합니다
        comment = Comment.objects.create(
            content=content,
            user=user,
            post=post
        )

        return Response({'message': '댓글이 성공적으로 작성되었습니다.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])  # 또는 ['PATCH']를 사용할 수 있습니다.
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(comment, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': '댓글이 성공적으로 수정되었습니다.'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def report(request):
    serializer = ReportSerializer(data=request.data)

    if serializer.is_valid():
        report_number = serializer.validated_data.get('report_number')
        report_type = serializer.validated_data.get('report_type')
        report_content = serializer.validated_data.get('report_content')
        reporter = serializer.validated_data.get('reporter')
        voice_phishing_record_id = serializer.validated_data.get('voice_phishing_record.id')

        # # 사용자 인스턴스를 가져옵니다
        # reporter_id = get_object_or_404(CustomUser, id=reporter_id.id)

        # 새로운 댓글 객체를 생성합니다
        report = Report.objects.create(
            report_number= report_number,
            report_type=report_type,
            report_content=report_content,
            reporter = reporter,
            voice_phishing_record_id=voice_phishing_record_id
        )

        return Response({'message': '성공적으로 신고되었습니다.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)