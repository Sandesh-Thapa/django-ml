from django.urls import path
from .views import MLAPIView

urlpatterns = [
    path('', MLAPIView.as_view())
]