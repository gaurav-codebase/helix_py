from django.urls import path
from .views import HelixView

urlpatterns = [
    path('helix/', HelixView.as_view(), name='helix'),
] 