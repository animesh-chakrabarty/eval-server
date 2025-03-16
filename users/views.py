from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
import util
from . import serializers

class Register(APIView):
    def post(self, request):
        try:
            # using the Meta class of serializer JSON is converted into users model
            serializer = serializers.UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            # create() method of the serializer is called - it hashes the password and saves the model into the db
            user = serializer.save()
            OTP = util.GenerateOTP()
            util.SendMail('OTP for Eval', f"Your OTP is {OTP}", [user.email])
            return util.JsonResponse(True, serializer.data, "user registered successfully", None)
        except ValidationError as e:
            return util.JsonResponse(False, e.detail, "validation error", None)
        except IntegrityError as e:
            return util.JsonResponse(False, str(e), "user already exists", None)
        except Exception as e:
            print(e)
            return util.JsonResponse(False, str(e), "something went wrong", None)