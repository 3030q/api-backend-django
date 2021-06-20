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
    json_dict = json.loads(request.body.decode('utf-8'))
    if json_dict['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in json_dict:
        if json_dict['type'] == 'url_verification':
            response_dict = {"challenge": json_dict['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in json_dict:
        event_msg = json_dict['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)
    if event_msg['type'] == 'message':
        user = event_msg['user']
        channel = event_msg['channel']
        response_msg = ":wave:, Hello <@%s>" % user
        client.chat_postMessage(channel='backend', text=response_msg)
        return HttpResponse(status=200)
    return HttpResponse(status=200)
