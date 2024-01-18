from rest_framework import serializers
from .models import Diagnosis

# class VoicePhishingRecordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VoicePhishingRecord
#         fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'