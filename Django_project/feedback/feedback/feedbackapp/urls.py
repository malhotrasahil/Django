from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='FeedHome'),
    path('about/', views.about, name='About'),
    path('thanks/', views.thanks, name='Thanks'),
]


