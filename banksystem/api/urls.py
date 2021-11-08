from django.urls import path
from .views import ClientList, ClientDetail


urlpatterns = [
    path('<int:pk>/', ClientDetail.as_view()),
    path('', ClientList.as_view()),
]