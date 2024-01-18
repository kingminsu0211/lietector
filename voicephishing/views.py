from rest_framework import generics
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# class VoicePhishingRecordListView(generics.ListCreateAPIView):
#     queryset = VoicePhishingRecord.objects.all()
#     serializer_class = VoicePhishingRecordSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class DiagnosisListView(generics.ListCreateAPIView):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

# @api_view(['POST'])
# def diagnose_voice(request):
#     serializer = DiagnosisSerializer(data=request.data)
#     if serializer.is_valid():
#         diagnosis_type = request.data.get('diagnosis_type')
#         call_details = request.data.get('call_details')
#         audio_file = request.FILES.get('audio_file')
#         if diagnosis_type == '직접 통화 내용 입력하기':
#
#             diagnosis = Diagnosis.objects.create(
#                 diagnosis_type=diagnosis_type,
#                 call_details=call_details,
#                 # audio_file=audio_file
#             )
#             return Response({'message': '성공적으로 입력되었습니다.'}, status=status.HTTP_201_CREATED)
#
#         if diagnosis_type == '통화 녹음본으로 입력하기':
#
#             diagnosis = Diagnosis.objects.create(
#                 diagnosis_type=diagnosis_type,
#                 audio_file=audio_file
#             )
#             return Response({'message': '성공적으로 업로드되었습니다.'}, status=status.HTTP_201_CREATED)
#
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def diagnose_voice(request):
    serializer = DiagnosisSerializer(data=request.data)
    if serializer.is_valid():
        diagnosis_type = serializer.validated_data.get('diagnosis_type')
        call_details = serializer.validated_data.get('call_details')
        audio_file = serializer.validated_data.get('audio_file')
        suspicion_percentage = serializer.validated_data.get('suspicion_percentage')

        if diagnosis_type == '직접 통화 내용 입력하기':
            # '직접 통화 내용 입력하기'일 경우 audio_file 필드는 무시
            serializer.validated_data.pop('audio_file', None)
            if call_details is None:
                return Response({'message':'잘못된 입력입니다.', 'data':serializer.data}, status=status.HTTP_201_CREATED)
            elif suspicion_percentage is None:
                return Response({'message': '퍼센트가 입력되지 않았습니다.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        elif diagnosis_type == '통화 녹음본으로 입력하기':
            # '통화 녹음본으로 입력하기'일 경우 call_details 필드는 무시
            serializer.validated_data.pop('call_details', None)
            if audio_file is None:
                return Response({'message':'업로드 되지 않았습니다.', 'data':serializer.data}, status=status.HTTP_201_CREATED)
            elif suspicion_percentage is None:
                return Response({'message': '퍼센트가 입력되지 않았습니다.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        serializer.save()

        if diagnosis_type == '직접 통화 내용 입력하기':
            return Response({'message': '성공적으로 입력되었습니다.', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        elif diagnosis_type == '통화 녹음본으로 입력하기':
            return Response({'message': '성공적으로 업로드되었습니다.', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
