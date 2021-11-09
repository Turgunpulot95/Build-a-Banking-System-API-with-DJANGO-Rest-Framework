from rest_framework import generics
from .models import *
from .serializers import *


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class ClientManagerList(generics.ListCreateAPIView):
    queryset = ClientManager.objects.all()
    serializer_class = ClientManagerSerializer


class ClientManagerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientManager.objects.all()
    serializer_class = ClientManagerSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TransferList(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class TransferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer


class WithdrawList(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class WithdrawDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer


class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class DepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer