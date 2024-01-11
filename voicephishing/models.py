from django.db import models
from django.contrib.auth.models import User
from user.models import CustomUser  # user 앱의 models 모듈에서 Accounts 클래스 import

class VoicePhishingRecord(models.Model):
    # 진단 유형 선택 옵션
    DIAGNOSIS_TYPE_CHOICES = [
        ('수사기관 사칭형', '수사기관 사칭형'),
        ('대출사기형', '대출사기형'),
    ]

    # 진단 유형
    diagnosis_type = models.CharField(
        max_length=50,
        choices=DIAGNOSIS_TYPE_CHOICES,
    )

    # 진단 결과 선택 옵션
    DIAGNOSIS_RESULT_CHOICES = [
        ('보이스피싱 의심', '보이스피싱 의심'),
        ('보이스피싱 안심', '보이스피싱 안심'),
        ('보이스피싱 확정', '보이스피싱 확정'),
        ('보이스피싱 여부 판단 못함', '보이스피싱 여부 판단 못함'),
    ]

    # 진단 결과
    diagnosis_result = models.CharField(
        max_length=100,
        choices=DIAGNOSIS_RESULT_CHOICES,
    )
    # 진단 일자 (자동으로 현재 일자와 시간이 저장됨)
    diagnosis_date = models.DateTimeField(auto_now_add=True)

    # 전화번호 정보 (Accounts 모델과의 외래키 관계)
    # number = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='voice_phishing_records')

    # 사용자 정보 (Django의 기본 User 모델과의 외래키 관계)
    # identify = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='voice_phishing_identifies')
    # reporter = models.ForeignKey(User, on_delete=models.CASCADE)