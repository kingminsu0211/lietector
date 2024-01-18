from django.db import models
from django.contrib.auth.models import User
from user.models import CustomUser  # user 앱의 models 모듈에서 Accounts 클래스 import
from django.conf import settings

# class VoicePhishingRecord(models.Model):
#     # 진단 유형 선택 옵션
#     DIAGNOSIS_TYPE_CHOICES = [
#         ('수사기관 사칭형', '수사기관 사칭형'),
#         ('대출사기형', '대출사기형'),
#     ]
#
#     # 진단 유형
#     diagnosis_type = models.CharField(
#         max_length=50,
#         choices=DIAGNOSIS_TYPE_CHOICES,
#     )
#
#     # 진단 결과 선택 옵션
#     DIAGNOSIS_RESULT_CHOICES = [
#         ('보이스피싱 의심', '보이스피싱 의심'),
#         ('보이스피싱 안심', '보이스피싱 안심'),
#         ('보이스피싱 확정', '보이스피싱 확정'),
#         ('보이스피싱 여부 판단 못함', '보이스피싱 여부 판단 못함'),
#     ]
#
#     # 진단 결과
#     diagnosis_result = models.CharField(
#         max_length=100,
#         choices=DIAGNOSIS_RESULT_CHOICES,
#     )
#     # 진단 일자 (자동으로 현재 일자와 시간이 저장됨)
#     diagnosis_date = models.DateTimeField(auto_now_add=True)
#
#     # 신고 번호
#     report_number = models.CharField(default='', max_length=20, blank=False)
#
#     # 사용자 정보 (Django의 기본 User 모델과의 외래키 관계)
#     # identify = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='voice_phishing_identifies')
#     reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')

class Diagnosis(models.Model):
    # 진단 유형 선택 옵션
    DIAGNOSIS_TYPE_CHOICES = [
        ('통화 녹음본으로 입력하기', '통화 녹음본으로 입력하기'),
        ('직접 통화 내용 입력하기', '직접 통화 내용 입력하기'),
    ]

    # 진단 유형
    diagnosis_type = models.CharField(
        max_length=50,
        choices=DIAGNOSIS_TYPE_CHOICES,
    )

    # 오디오 업로드
    audio_file = models.FileField(upload_to='voice_recordings/',null=True, blank=True)

    #통화내용 입력
    call_details = models.TextField(null=True, blank=True)

    # 진단 일자 (자동으로 현재 일자와 시간이 저장됨)
    diagnosis_date = models.DateTimeField(auto_now_add=True)


    suspicion_percentage = models.FloatField(null=True,blank=True)

    def diagnose(self):
        # 여기에서 보이스피싱 진단 알고리즘을 구현합니다.
        # 예를 들어, 간단한 더미 알고리즘으로 설정하겠습니다.
        self.suspicion_percentage = 50.0
        self.save()