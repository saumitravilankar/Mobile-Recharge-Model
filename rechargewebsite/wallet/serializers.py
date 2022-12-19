from rest_framework.serializers import ModelSerializer
from .models import *

# class UserSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'

class DebitCardSerializer(ModelSerializer):

    class Meta:
        model = DebitCard
        fields = ['id','card_number','balance','expiration_date','cvv','card_owner']

class WalletSerializer(ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['user','balance','timestamp']