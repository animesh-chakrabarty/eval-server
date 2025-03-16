from django.shortcuts import render
from util import CustomJsonResponse

def test(request):
    return CustomJsonResponse.send(True, None, "users working", None)
