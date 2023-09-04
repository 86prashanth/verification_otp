from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from Verification_Otp.helpers import send_otp_to_phone
from Verification_Otp.models import User
# Create your views here.
@api_view(['POST'])
def send_otp(request):
    data=request.data
    if data.get('phone_number') is None :
        return Response({
            'status':400,
            'message':'key phone_number is required'
        })
        
    if data.get('password') is None:
        return Response({
            'status':400,
            'message':'key password is required'
        })
    try:
        user=User.objects.create(
            phone_number=data.get('phone_number'),
            otp=send_otp_to_phone(data.get('phone_number'))
            )
        user.set_password=data.get('set_password')
        user.save()
    except Exception as e:
            return Response({
                'status':200,
                'message':'Otp has been sent'
            })
    
@api_view(['POST'])
def verify_otp(request):
    data=request.data
    if data.get('phone_number') is None :
        return Response({
            'status':400,
            'message':'key phone_number is required'
        })
        
    if data.get('otp') is None:
        return Response({
            'status':400,
            'message':'key otp is required'
        })
    try:   
        user=User.objects.create(phone_number=data.get('phone_number'))
    except Exception as e:
        return Response({
            "status":400,
            "message": "invalid phone"
        })
    if user.otp==data.get('otp'):
        return Response({
            "status":200,
            "message":"otp has been matched"
        })
    return Response({
            "status":400,
            "message":"invalid otp"
        })
    

    

