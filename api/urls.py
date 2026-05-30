from django.urls import path
from django.views.generic import TemplateView
from .views import health_check

app_name = 'api'

urlpatterns = [
    path('health/', health_check, name='health_check'),
    # Add your API endpoints here
]
