import json

import slack
import os
from pathlib import Path

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from rest_framework.decorators import api_view

from api_backend_parser import settings


@api_view(['Post'])
def hello(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    client.chat_postMessage(channel='#backend', text='Titatutu')
    return HttpResponse(status=200)
