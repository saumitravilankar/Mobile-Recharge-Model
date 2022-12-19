from rest_framework import serializers
from .models import Recharge, Plan

class RechargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recharge
        fields = ['phone_number','type','operator','circle','plan']

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['id','topup_amount','talktime','validity_in_days']