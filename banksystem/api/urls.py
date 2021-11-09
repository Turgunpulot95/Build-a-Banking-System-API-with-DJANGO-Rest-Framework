from django.urls import path
from .views import *


urlpatterns = [
    path('clients/<int:pk>/', ClientDetail.as_view()),
    path('clients/', ClientList.as_view()),

    path('branches/<int:pk>/', BranchDetail.as_view()),
    path('branches/', BranchList.as_view()),

    path('banks/<int:pk>/', BankDetail.as_view()),
    path('banks/', BankList.as_view()),

    path('clientmanagers/<int:pk>/', ClientManagerDetail.as_view()),
    path('clientmanagers/', ClientManagerList.as_view()),

    path('accounts/<int:pk>/', AccountDetail.as_view()),
    path('accounts/', AccountList.as_view()),

    path('transfer/<int:pk>/', TransferDetail.as_view()),
    path('transfer/', TransferList.as_view()),

    path('withdraw/<int:pk>/', WithdrawDetail.as_view()),
    path('withdraw/', WithdrawList.as_view()),

    path('deposits/<int:pk>/', DepositDetail.as_view()),
    path('deposits/', DepositList.as_view()),
]