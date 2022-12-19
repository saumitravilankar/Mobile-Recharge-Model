from django.shortcuts import render
from django.http import JsonResponse

import random

from .models import Plan
from wallet.models import Wallet

from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
def create_plan(request):

    for i in range(1,26):
        topup_amount = random.randint(50,1000)
        talktime = topup_amount*0.875
        plan = Plan.objects.create(topup_amount=topup_amount,talktime=talktime)
        plan.save()

    return JsonResponse('25 plans created',safe=False)

    # To delete all plans
    # plan = Plan.objects.all()
    # plan.delete()
    # return JsonResponse('plans deleted',safe=False)

@api_view(['GET'])
def plan_list(request):

    plan = Plan.objects.all()
    serializers = PlanSerializer(plan, many=True)
    return Response(serializers.data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def recharge(request):

    if request.method == 'GET':

        recharge = Recharge.objects.filter(user=request.user)
        serializer = RechargeSerializer(recharge, many=True)
        return Response(serializer.data)


    if request.method == 'POST':

        serializer = RechargeSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            # print('validated')
            serializer.save(user=request.user)

            plan = Plan.objects.get(id=request.data.get('plan'))
            wallet = Wallet.objects.get(user=request.user)

            wallet.balance -= int(plan.topup_amount)
            wallet.save()


            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        


