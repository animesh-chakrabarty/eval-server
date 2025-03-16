import util
from django.shortcuts import render

def test(request):
    return util.JsonResponse(True, None, "users working", None)
