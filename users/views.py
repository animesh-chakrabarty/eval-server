from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
import util
from . import serializers
from . import models

class Register(APIView):
    def post(self, request):
        try:
            serializer = serializers.UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            OTP = util.GenerateOTP()
            OTPInstance, created = models.UserOTPMapping.objects.update_or_create(userId=user, defaults={'OTP': OTP})
            util.SendMail('OTP for Eval', f"Your OTP is {OTP}", [user.email])
            return util.JsonResponse(True, serializer.data, f"mail with OTP sent to {user.email} ", None)
        except ValidationError as e:
            return util.JsonResponse(False, e.detail, "validation error", None)
        except IntegrityError as e:
            return util.JsonResponse(False, str(e), "user already exists", None)
        except Exception as e:
            return util.JsonResponse(False, str(e), "something went wrong", None)
        
class VerifyOTP(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            OTP = request.data.get('OTP')
            if not email or not OTP:
                return util.JsonResponse(False, None, "Email & OTP are required", None)

            user = models.User.objects.filter(email=email).first()
            if not user:
                return util.JsonResponse(False, None, f"User not found with email {email}", None)
            
            retrievedOTP = models.UserOTPMapping.objects.filter(userId=user.id).first()
            if retrievedOTP.OTP != OTP:
                return util.JsonResponse(False, None, "OTP doesn't match", None)
            
            user.is_active = True;
            user.save()
            retrievedOTP.delete()

            return util.JsonResponse(True, None, "OTP verified successfully! Account activated", None)
        
        except Exception as e:
            return util.JsonResponse(False, str(e), "Something went wrong.", None)
