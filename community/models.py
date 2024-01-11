from django.db import models
from django.contrib.auth.models import User
from user.models import CustomUser
from voicephishing.models import VoicePhishingRecord
from django.conf import settings


class Post(models.Model):
    # 글 제목
    title = models.CharField(max_length=100)
    # 글 내용
    content = models.TextField()
    # 생성 일자 (자동으로 현재 일자와 시간이 저장됨)
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트 일자
    updated_at = models.DateTimeField(auto_now=True)
    # 의심 전화 번호 입력(선택사항)
    report_number = models.CharField(max_length=11, blank=True, null=True)
    # 글 작성자 정보
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    # 댓글 내용
    content = models.TextField()
    # 댓글 작성 일자 (자동으로 현재 일자와 시간이 저장됨)
    created_at = models.DateTimeField(auto_now_add=True)
    # 댓글 작성자 정보 (Django의 기본 User 모델과의 외래키 관계)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 댓글이 달린 글 정보 (Post 모델과의 외래키 관계)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Report(models.Model):
    # 신고 유형
    report_type = models.CharField(max_length=50)

    # 신고 내용
    report_content = models.TextField()

    # 신고 일자 (자동으로 현재 일자와 시간이 저장됨)
    report_date = models.DateTimeField(auto_now_add=True)

    # # 신고자 정보 (Django의 기본 User 모델과의 외래키 관계)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 음성피싱 기록 정보 (VoicePhishingRecord 모델과의 외래키 관계)
    voice_phishing_record = models.ForeignKey(VoicePhishingRecord,default='', on_delete=models.CASCADE)