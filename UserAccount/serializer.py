from rest_framework import serializers
from .models import userAccountModel
from datetime import datetime,timedelta
from django.conf import settings
from twilio.rest import Client
import random
from django.utils import timezone

import os
from dotenv import load_dotenv
load_dotenv()

class UserAcountSerializer(serializers.ModelSerializer):
    # password1 = serializers.CharField(write_only = True,min_length = 6)
    # password2 = serializers.CharField(write_only = True,min_length = 6)
    otp = serializers.CharField(write_only = True , allow_null=True, allow_blank=True)
    class Meta:
        model = userAccountModel
        fields = [

            

            'id','name','Phone_no','password','otp'

        ]
    
    
    "this create function is used for hash(encript) the password field "
    def create(self, validated_data):
        Otp = random.randint(1000,9999)
        Otp_expre_at = timezone.now() + timedelta(minutes=10)
        Phone_no = int(validated_data['Phone_no']),
        user = userAccountModel(
            name = validated_data['name'],
            # Email = validated_data['Email'],
            Phone_no = validated_data['Phone_no'],
            Otp = Otp,
            Otp_expre_at = Otp_expre_at,
            Maximum_otp_try = settings.MAX_OTP_TRY
        )
        user.set_password(validated_data['password'])
        user.save()
        try:

            account_sid = os.environ.get('ACCOUNT_SSID')
            auth_token =os.environ.get('AUTH_TOKEN') 

         

            client = Client(account_sid, auth_token)
            message = client.messages.create(
            body=f'Hello your Otp is {Otp}',
            from_='+17603024639',
            to=f'+251{Phone_no}'
            )
            print(message.sid)
        except:
            print('some thing went wrong try again ')
        return user