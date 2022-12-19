from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import *
from .serializers import *

# Create your views here.
@api_view(['POST']) #Create proper abstractuser with all fields to use GET to otherwise its too complicated.
def create_user_with_wallet(request):

    if request.method == 'POST':

        if request.data.get('username') is None:
            return Response({
                'status': 400,
                'message': 'username is required'
            })
        
        if request.data.get('password') is None:
            return Response({
                'status': 400,
                'message': 'password is required'
            })
        
        if request.data.get('phone_number') is None:
            return Response({
                'status': 400,
                'message': 'phone_number is required'
            })
        
        user = User.objects.create(username=request.data.get('username'),phone_number=request.data.get('phone_number'))
        user.set_password(request.data.get('password'))
        user.save()

        return Response({'status':200, 'message':'User Created'})

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def create_debit_card(request):

    if request.method == 'GET':

        cards = DebitCard.objects.filter(user=request.user)
        serializer = DebitCardSerializer(cards, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        serializer = DebitCardSerializer(data=request.data)

        if serializer.is_valid():
            # serializer = serializer.validated_data
            # serializer.user = request.user
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wallet(request):

    wallet = Wallet.objects.get(user=request.user)
    serializer = WalletSerializer(wallet)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def wallet_recharge(request):
   
    card_number = request.data.get('card_number')
    expiration_date = request.data.get('expiration_date')
    cvv = request.data.get('cvv')
    card_owner = request.data.get('card_owner')
    amount = request.data.get('amount')
    amount = int(amount)

    wallet = Wallet.objects.get(user=request.user)
    card = DebitCard.objects.get(user=request.user,card_number=card_number)

    if (card.expiration_date == expiration_date and card.cvv == cvv and card.card_owner == card_owner and card.balance >= amount):
            print('ifpass')
            card.balance -= amount
            card.save()
            wallet.balance += amount
            wallet.save()
            print('added')
            return Response({
                'status':200,
                'message':'Wallet credited.',
                'wallet balance': wallet.balance
            })
