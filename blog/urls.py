from django.urls import path 
from .views import HomeView,DetailsView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<int:pk>/', DetailsView.as_view(),name='detail')
]