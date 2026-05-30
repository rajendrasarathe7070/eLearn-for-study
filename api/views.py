from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from datetime import datetime

# Create your views here.

@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint to keep server alive on Render.
    Returns server status and timestamp.
    """
    return JsonResponse({
        'status': 'ok',
        'message': 'Server is running',
        'timestamp': datetime.now().isoformat(),
        'service': 'eLearn-for-study'
    })
