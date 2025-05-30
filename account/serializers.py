from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.tokens import PasswordResetTokenGenerator, default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import force_bytes, smart_str, DjangoUnicodeDecodeError
from rest_framework_simplejwt.tokens import RefreshToken
from account.utils import Util



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ('email', 'name', 'tc', 'password', 'password2')

        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password does not match")
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    
    
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name')

class UserPasswordChangeSerializer(serializers.Serializer):
   password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
   password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
   class Meta:
       fields = ('password', 'password2')
       extra_kwargs = {
           'password': {
               'write_only': True,
           },
           'password2': {
               'write_only': True,
           },
       }
   def validate(self, attrs):
       password = attrs.get('password')
       password2 = attrs.get('password2')
       user = self.context.get('user')
       if password != password2:
           raise serializers.ValidationError("Password and Confirm Password does not match")
       
       user.set_password(password)
       user.save()
       return attrs

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ('email',)
        extra_kwargs = {
            'email': {
                'write_only': True,
            },
        }
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            email = attrs.get('email')
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            link = f"http://localhost:8000/api/user/reset-password/{uid}/{token}/"
            print('Encode id:', uid)
            print('Token:', token)
            print('Password Reset Link:', link)
            # send_email()
            data = {
               'email_subject': 'Reset your password',
                'email_body': f'Click the link to reset your password: {link}',
                'to_email': user.email,
                
             }
            Util.send_email(data)
            return attrs
        else:
            raise serializers.ValidationError("Email does not exist")

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    class Meta:
        fields = ('password', 'password2')
      
    
 
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password does not match")
            
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not default_token_generator.check_token(user,token):
                raise serializers.ValidationError("Token is not valid or expired")

            
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
         raise serializers.ValidationError("Token is not valid or expired")
        except User.DoesNotExist:
         raise serializers.ValidationError("User not found for this reset link")
   
