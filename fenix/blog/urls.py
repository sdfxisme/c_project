from django.urls import path

from .views import *

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('emitent/<str:slug>/', CoinsByEmitent.as_view(), name='emitent'),
    path('type/<str:slug>/', CoinsByType.as_view(), name='type'),
    path('tag/<str:slug>/', CoinsByTag.as_view(), name='tag'),
    path('sale/', CoinsBySale.as_view(), name='sale'),
    path('coin/<str:slug>/', GetCoin.as_view(), name='coin'),
    path('search/', Search.as_view(), name='search'),
    path('coin/v11111/', GetCoin.as_view(), name='coin1'),
    ]