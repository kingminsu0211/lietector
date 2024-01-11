from rest_framework import viewsets

from .serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import SignupSerializer

class CheckAccountViewset(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AccountsSerializer

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    print("Request Data:", request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        last_name=serializer.validated_data['last_name']
        first_name=serializer.validated_data['first_name']
        nickname = serializer.validated_data['nickname']
        number = serializer.validated_data['number']

        # Check if the username is unique
        # if CustomUser.objects.filter(username=username).exists():
        #     return Response({'error': '이미 존재하는 id입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the nickname is unique
        # if CustomUser.objects.filter(nickname__iexact=nickname).exists():
        #     return Response({'error': '이미 존재하는 nickname입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the number is unique
        # if CustomUser.objects.filter(number=number).exists():
        #     return Response({'error': '이미 존재하는 전화번호입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create a new user
            user = CustomUser.objects.create_user(username=username, password=password,last_name=last_name,first_name=first_name,nickname=nickname,number=number)
        except ValidationError as e:
            return Response({'error': e.message}, status=status.HTTP_400_BAD_REQUEST)

        # Log in the user
        login(request, user)

        return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
