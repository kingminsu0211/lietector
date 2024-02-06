from rest_framework import serializers
from .models import Post, Comment, Report, Ask, AskComment
from user.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    def get_user_nickname(self, obj):
        return obj.user.nickname
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at', 'updated_at', 'report_number','writer']

class CommentSerializer(serializers.ModelSerializer):
    def get_user_nickname(self, obj):
        return obj.user.nickname
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields= ['post','user_nickname']

class ReportSerializer(serializers.ModelSerializer):
    def get_user_nickname(self, obj):
        return obj.user.nickname
    class Meta:
        model = Report
        fields = ['report_number','report_type', 'report_content', 'report_date','reporter','voice_phishing_record']

class AskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields = "__all__"

class AskCommentSerializer(serializers.ModelSerializer):
    def get_user_nickname(self, obj):
        return obj.user.nickname
    class Meta:
        model = AskComment
        fields = '__all__'
        read_only_fields = ['post','user_nickname']
