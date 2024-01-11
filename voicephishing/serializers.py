from rest_framework import serializers
from .models import VoicePhishingRecord

class VoicePhishingRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoicePhishingRecord
        fields = ['diagnosis_type', 'diagnosis_result', 'diagnosis_date']
