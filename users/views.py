from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.db.utils import IntegrityError
from util import CustomJsonResponse
from . import serializers

class Register(APIView):
    def post(self, request):
        try:
            # using the Meta class of serializer JSON is converted into users model
            serializer = serializers.UserSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            # create() method of the serializer is called - it hashes the password and saves the model into the db
            serializer.save()
            return CustomJsonResponse.send(True, serializer.data, "user registered successfully", None)
        except ValidationError as e:
            return CustomJsonResponse.send(False, e.detail, "validation error", None)
        except IntegrityError as e:
            return CustomJsonResponse.send(False, str(e), "user already exists", None)
        except Exception as e:
            return CustomJsonResponse.send(False, str(e), "something went wrong", None)