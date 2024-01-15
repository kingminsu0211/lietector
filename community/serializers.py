from rest_framework import serializers
from .models import Post
from .models import Comment
from .models import Report
from user.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at', 'report_number','writer']

class CommentSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())  # CustomUser 모델에 맞게 변경
    # post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['report_number','report_type', 'report_content', 'report_date','reporter','voice_phishing_record']
