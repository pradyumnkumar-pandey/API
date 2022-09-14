from datetime import datetime,timedelta,timezone,date
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from django.urls import reverse
from django.shortcuts import redirect

URLS=['/api3/user_login/']

class UserAgeVerification:
    def __init__(self, get_response):
        self.get_response= get_response
    
    def __call__(self,request):
        response=self.get_response(request)
        if request.path in URLS:
            user=request.user
            if user.is_authenticated:
                dob=user.dob
                
                date_today=str(datetime.today()).split(" ")[0]
                date_split=date_today.split('-')
                date_split=date(int(date_split[0]),int(date_split[1]),int(date_split[2]))
                
                number_of_days=date_split-dob
                number_of_days=str(number_of_days).split(" ")[0]
                print(number_of_days)
                if int(number_of_days)>6574:
                    return response
                else:
                    return HttpResponse("Age Is Less Than 18 Years, You Cannot Login")
                    #return HttpResponse({'Error':"Age is Less"},status=status.HTTP_403_FORBIDDEN)
                    #return redirect(reverse('user_login'))
            else:
                return response
        else:
            return response
