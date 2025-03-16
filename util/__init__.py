from .JsonResponse import JsonResponse
from .GenerateOTP import GenerateOTP
from .Mail import SendMail

class util:
    JsonResponse = staticmethod(JsonResponse)
    GenerateOTP = staticmethod(GenerateOTP)
    SendMail = staticmethod(SendMail)