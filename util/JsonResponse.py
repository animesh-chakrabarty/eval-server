from django.http import JsonResponse as JsonResponseInBuilt

def JsonResponse(success: bool, data, message, extraData):
        res = {
            'success': success,
            'data': data,
            'message': message,
            'extraData': extraData
        }

        return JsonResponseInBuilt(res)