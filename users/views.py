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
            print(OTPInstance, created)
            util.SendMail('OTP for Eval', f"Your OTP is {OTP}", [user.email])
            return util.JsonResponse(True, serializer.data, "user registered successfully", None)
        except ValidationError as e:
            return util.JsonResponse(False, e.detail, "validation error", None)
        except IntegrityError as e:
            return util.JsonResponse(False, str(e), "user already exists", None)
        except Exception as e:
            print(e)
            return util.JsonResponse(False, str(e), "something went wrong", None)