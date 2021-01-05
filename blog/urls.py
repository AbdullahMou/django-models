from django.urls import path 
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<int:pk>/', DetailsView.as_view(),name='detail'),
    path('add/', Create_view.as_view(),name='add'),
    path('<int:pk>/update/', Update_view.as_view(),name='update'),
    path('<int:pk>/delete/', Delete_view.as_view(),name='delete'),
]