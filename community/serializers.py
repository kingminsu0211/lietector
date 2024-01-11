from rest_framework import serializers
from .models import Post
from .models import Comment
from .models import Report

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at', 'report_number','writer']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['report_type', 'report_content', 'report_date','reporter','voice_phishhing_record']
