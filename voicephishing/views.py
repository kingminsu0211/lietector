
from rest_framework import generics
from .serializers import *


class VoicePhishingRecordListView(generics.ListCreateAPIView):
    queryset = VoicePhishingRecord.objects.all()
    serializer_class = VoicePhishingRecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VoicePhishingRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoicePhishingRecord.objects.all()
    serializer_class = VoicePhishingRecordSerializer
