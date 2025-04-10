from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import(
                                UserRegistrationSerializer, 
                                UserLoginSerializer, 
                                UserProfileSerializer, 
                                UserPasswordChangeSerializer,
                                SendPasswordResetEmailSerializer,
                                UserPasswordResetSerializer
                                )
from django.contrib.auth import authenticate
from account.renders import UserRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistrationView(APIView):
    renderer_classes = [UserRender]
    def post(self,request,formate=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           token = get_tokens_for_user(user)
           return Response({
               "token":token,
               "mgs":"User registration successfully"
               }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    renderer_classes = [UserRender]
    def post(self,request,formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')  # ✅ fixed here
            password = serializer.validated_data.get('password')  # ✅ fixed here
            print(email,password)
            user = authenticate(email=email,password=password)
            if user:
                token = get_tokens_for_user(user)
                return Response({
                    "token":token,
                    "mgs":"User login successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"erors": {"non_fields_error":["Email or password doesn't match"]}}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def get(self,request,formate=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def post(self,request,formate=None):
        serializer = UserPasswordChangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
           
              return Response({"mgs":"Password changed successfully"}, status=status.HTTP_200_OK)
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRender]
    def post(self,request,formate=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            
            return Response({"mgs":"Password reset link has been sent to your email"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(APIView):
    renderer_classes = [UserRender]
    def post(self,request,uidb64,token,formate=None):
        serializer = UserPasswordResetSerializer(
            data = request.data,
            context = {
                'uid':uidb64,
                'token':token
            }
        )
        if serializer.is_valid(raise_exception=True):
            return Response({"mgs":"Password reset successfully"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)