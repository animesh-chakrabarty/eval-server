from django.http import JsonResponse

def send(success: bool, data, message, extraData):
    res = {
        'success': success,
        'data': data,
        'message': message,
        'extraData': extraData
    }

    return JsonResponse(res)