from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.
# @parser_classes((CustomJSONParser,))
@parser_classes((JSONParser,))
class TypeformSubmissions(APIView):
    """Typeform webhook to receive data from every submission to
        the typeforms and save the user's progress on DB
    """
    permission_classes = [AllowAny]
    
    def verifySignature(self, receivedSignature: str, payload):
        WEBHOOK_SECRET = settings.TYPEFORM_CLIENT_SECRET
        digest = hmac.new(
            WEBHOOK_SECRET.encode("utf-8"), payload.encode("utf-8"), hashlib.sha256
        ).digest()
        e = base64.b64encode(digest).decode()
    
        if e == receivedSignature:
            return True
        return False
    
    # @csrf_exempt
    def post(self, request, *args, **kwargs):
        body = request.data
        
        receivedSignature = request.headers.get("typeform-signature")
        
        if receivedSignature is None:
            return Response(
                {"Fail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )
        
        sha_name, signature = receivedSignature.split("=", 1)
        if sha_name != "sha256":
            return Response(
                {"Fail": "Operation not supported."},
                status=status.HTTP_501_NOT_IMPLEMENTED,
            )
            
        is_valid = self.verifySignature(signature, request.raw_body)
        if is_valid != True:
            return Response(
                {"Fail": "Invalid signature. Permission Denied."},
                status=status.HTTP_403_FORBIDDEN,
            )
            
        save_typeform_data(body)
        
        return Response({}, status=status.HTTP_200_OK)