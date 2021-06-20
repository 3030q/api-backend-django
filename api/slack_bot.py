import json

import slack
import os
from pathlib import Path

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from rest_framework.decorators import api_view

from api.models import App
from api.serializer import AppSerializer
from api_backend_parser import settings

@api_view(['Post'])
def hello(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    data = request.data
    print(data)
    if data['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in data:
        if data['type'] == 'url_verification':
            response_dict = {"challenge": data['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in data:
        event_msg = data['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)
    name, platform = tuple(data['text'].split())
    print(name, platform)
    response_msg = ":wave:, Hello aboba"
    client.chat_postMessage(channel='#reviewgator-chat', text=response_msg)
    return HttpResponse(status=200)


@api_view(['Post'])
def last_week_statistics(request):
    client = slack.WebClient(token=settings.BOT_USER_ACCESS_TOKEN)
    data = request.data
    print(data)
    if data['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in data:
        if data['type'] == 'url_verification':
            response_dict = {"challenge": data['challenge']}
            return JsonResponse(response_dict, safe=False)
    if 'event' in data:
        event_msg = data['event']
        if ('subtype' in event_msg) and (event_msg['subtype'] == 'bot_message'):
            return HttpResponse(status=200)
    name, platform = tuple(data['text'].split())
    app = App.objects.filter(name=name, platform=platform).get()
    print(AppSerializer(app))
    response_msg = ":wave:, Hello abobus"
    client.chat_postMessage(channel='#reviewgator-chat', text=response_msg)
    return HttpResponse(status=200)
