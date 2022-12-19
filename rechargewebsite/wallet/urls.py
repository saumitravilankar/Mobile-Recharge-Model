from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns = [
    path('wallet/',views.wallet,name='wallet'),
    path('home/create_user/',views.create_user_with_wallet,name='create_user'),
    path('wallet/add/debit_card/',views.create_debit_card,name='add_debitcard'),
    path('wallet/addmoney/',views.wallet_recharge,name='wallet_recharge'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
