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
    with open('ccc.json', 'w') as file:
        file.write(json.dumps(json_dict))

    if json_dict['token'] != settings.VERIFICATION_TOKEN:
        return HttpResponse(status=403)
    if 'type' in json_dict:
        if json_dict['type'] == 'url_verification':
            response_dict = {"challenge": json_dict['challenge']}
            return JsonResponse(response_dict, safe=False)
    if json_dict['command'] == '/hello_review_gator':
        response_msg = ":wave:, Hello me"
        client.chat_postMessage(channel='#backend', text=response_msg)

        return HttpResponse(status=200)
    return HttpResponse(status=200)
